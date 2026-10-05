"""Parse the workout logs in data/ into data.js for index.html.

Usage: python parse.py
"""
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
DATA_DIR = ROOT / "data"
OUT = ROOT / "data.js"

BODYWEIGHT = 78  # kg, added to the logged weight of bodyweight exercises
TORSO_CC_ROW_CUTOFF = 40  # torso "cc" at or above this weight is a mislabeled cable row

# (split, abbreviation) -> exercise id
ABBREVIATIONS = {
    ("arms", "sp"): "shoulder_press",
    ("arms", "dp"): "shoulder_press",  # typo
    ("arms", "sc"): "skull_crusher",
    ("arms", "sq"): "skull_crusher",  # typo
    ("arms", "cc"): "cable_curl",
    ("arms", "bc"): "barbell_curl",
    ("arms", "te"): "tricep_extension",
    ("arms", "tp"): "tricep_pushdown",
    ("arms", "lr"): "lateral_raise",
    ("arms", "cr"): "lateral_raise",  # typo
    ("arms", "di"): "dips",
    ("arms", "hc"): "hammer_curl",
    ("torso", "bp"): "bench_press",
    ("torso", "cr"): "cable_row",
    ("torso", "cc"): "cable_crunch",  # or cable_row, see TORSO_CC_ROW_CUTOFF
    ("torso", "dp"): "incline_db_press",
    ("torso", "pl"): "pull_up",
    ("torso", "pu"): "pull_up",
    ("torso", "ps"): "push_up",
    ("torso", "pd"): "lat_pulldown",
    ("torso", "cp"): "incline_bench",
    ("torso", "oh"): "overhead_press",
    ("torso", "bl"): "barbell_row",
    ("torso", "ab"): "abs",
    ("torso", "pp"): None,  # one-off machine, ignored
    ("legs", "sq"): "squat",
    ("legs", "rd"): "romanian_deadlift",
    ("legs", "cr"): "calf_raise",
    ("legs", "lr"): "leg_raise",
    ("legs", "cc"): "cable_crunch",
    ("legs", "hc"): "hammer_curl",
    ("legs", "le"): "leg_extension",
}

# exercise id -> (display name, is bodyweight)
EXERCISES = {
    "shoulder_press": ("Shoulder DB press", False),
    "skull_crusher": ("Skull crusher", False),
    "cable_curl": ("Cable curl", False),
    "barbell_curl": ("Barbell curl", False),
    "tricep_extension": ("Tricep extension", False),
    "tricep_pushdown": ("Tricep pushdown", False),
    "lateral_raise": ("Lateral DB raise", False),
    "dips": ("Dips", True),
    "hammer_curl": ("Hammer curl", False),
    "bench_press": ("Bench press", False),
    "cable_row": ("Cable row", False),
    "incline_db_press": ("Incline DB press", False),
    "pull_up": ("Pull-up", True),
    "push_up": ("Push-up", True),
    "lat_pulldown": ("Lat pulldown", False),
    "incline_bench": ("Incline bench press", False),
    "overhead_press": ("Overhead press", False),
    "barbell_row": ("Barbell row", False),
    "abs": ("Abs", True),
    "squat": ("Squat", False),
    "romanian_deadlift": ("Romanian deadlift", False),
    "calf_raise": ("Calf raise", False),
    "leg_raise": ("Leg raise", False),
    "cable_crunch": ("Cable crunch", False),
    "leg_extension": ("Leg extension", False),
}

HEADER_RE = re.compile(r"^(\d{2})(\d{2})\s+([a-z]+)\s*$")
LINE_RE = re.compile(r"^([a-z]{2})\s+(.+)$")


def parse_sets(text):
    """'80.6/70.7,4' -> [(80, 6), (70, 7), (70, 4)]. Raises ValueError if unreadable."""
    sets = []
    for segment in text.split("/"):
        weight, _, reps = segment.partition(".")
        if not reps:
            raise ValueError(f"no reps in segment {segment!r}")
        # Tolerate typos: "9.8" for "9,8", trailing commas, stray letters.
        reps = re.sub(r"[^\d,.]", "", reps).replace(".", ",")
        rep_counts = [int(r) for r in reps.split(",") if r]
        if not rep_counts:
            raise ValueError(f"no reps in segment {segment!r}")
        sets += [(float(weight), r) for r in rep_counts]
    return sets


def parse_file(path, warnings):
    year = int(re.search(r"(\d{4})", path.stem).group(1))
    entries = []
    split = day = None
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        where = f"{path.name}:{lineno}"
        if m := HEADER_RE.match(line):
            dd, mm, split = int(m[1]), int(m[2]), m[3]
            try:
                day = date(year, mm, dd)  # dates are DDMM
            except ValueError:
                warnings.append(f"{where}: invalid date in header {line!r}")
                day = None
            continue
        m = LINE_RE.match(line)
        if not m or day is None:
            warnings.append(f"{where}: unreadable line {line!r}")
            continue
        abbr, set_text = m[1], m[2].replace(" ", "")
        if (split, abbr) not in ABBREVIATIONS:
            warnings.append(f"{where}: unknown exercise {abbr!r} on {split} day")
            continue
        try:
            sets = parse_sets(set_text)
        except ValueError as e:
            warnings.append(f"{where}: {e} in {line!r}")
            continue
        exercise = ABBREVIATIONS[(split, abbr)]
        if split == "torso" and abbr == "cc":
            exercise = "cable_row" if sets[0][0] >= TORSO_CC_ROW_CUTOFF else "cable_crunch"
        if exercise is None:
            continue
        entries.append((exercise, split, day, line, sets))
    return entries


def main():
    warnings = []
    entries = []
    for path in sorted(DATA_DIR.glob("*.txt")):
        entries += parse_file(path, warnings)

    by_exercise = {}
    for exercise, split, day, line, sets in entries:
        rows = by_exercise.setdefault(exercise, [])
        if any(r[1] == day for r in rows):
            warnings.append(f"{day.isoformat()}: {line!r} logged twice that day, kept the first entry")
            continue
        rows.append((split, day, line, sets))

    exercises = []
    for ex_id, rows in by_exercise.items():
        name, is_bodyweight = EXERCISES[ex_id]
        splits = [r[0] for r in rows]
        rows.sort(key=lambda r: r[1])
        exercises.append({
            "id": ex_id,
            "name": name,
            "split": max(set(splits), key=splits.count),
            "bodyweight": is_bodyweight,
            "sessions": [
                {
                    "date": day.isoformat(),
                    "raw": line,
                    "sets": [[w + BODYWEIGHT if is_bodyweight else w, r] for w, r in sets],
                }
                for _, day, line, sets in rows
            ],
        })

    out = {"bodyweight": BODYWEIGHT, "exercises": exercises, "warnings": warnings}
    OUT.write_text("window.WORKOUT_DATA = " + json.dumps(out, indent=1) + ";\n", encoding="utf-8")

    print(f"Wrote {OUT.name}: {len(entries)} entries across {len(exercises)} exercises")
    for ex in sorted(exercises, key=lambda e: -len(e["sessions"])):
        print(f"  {len(ex['sessions']):4d}  {ex['name']} ({ex['split']})")
    if warnings:
        print(f"{len(warnings)} warning(s):")
        for w in warnings:
            print("  " + w)


if __name__ == "__main__":
    main()
