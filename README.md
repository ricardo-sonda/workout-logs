# Workout logs

**[See the charts →](https://ricardo-sonda.github.io/workout-logs/)**

This is how strong I've been getting since January 2025, charted from text files I type in the gym between sets. I have data dating back to 2023 but I can't be bothered to parse that.  

## What you're looking at

One chart per exercise, grouped by Torso / Arms / Legs. Each dot is a session. The line is a rolling average, so a single bad day doesn't count. Several bad days do.

The score is an estimated 1-rep max (or volume, or top weight; there's a dropdown). The first set of a session counts most and later sets count less, because the first set is who I am and the later ones are who I become.

## Notes to future me

- Log workouts in `data/Workout log YYYY.txt`. The format is in [parsing-info.md](parsing-info.md).
- Run `python parse.py`, then commit and push `data.js`. The site updates by itself a minute later.
- `parse.py` complains about lines it can't read. Listen to it.
- Bodyweight is hardcoded at 78 kg, approximately, and selectively measured.
- Exercises logged fewer than 8 times don't get a chart. Overhead press, I saw what you did.
