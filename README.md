# Workout logs

**[See the charts →](https://ricardo-sonda.github.io/workout-logs/)**

This is how strong I've been getting since January 2025, charted from text files I type in the gym between sets. I have data dating back to 2023 but I can't be bothered to parse that.  

## What you're looking at

One chart per exercise, grouped by Torso / Arms / Legs. Each dot is a session. The line is a rolling average, so a single bad day doesn't count. Several bad days do.

The score is an estimated 1-rep max (or volume, or top weight; there's a dropdown). The first set of a session counts most and later sets count less, because the first set is who I am and the later ones are who I become.

## Market commentary

*Q3 2026 outlook. Based on Epley 1RM, 5-session rolling average. Not financial advice. Barely fitness advice.*

**Macro.** Overall, the portfolio is up. The central bank has held bodyweight at 78 kg for seven consecutive quarters, and analysts suspect it has simply stopped checking. Session allocation is still lopsided (Torso 101, Arms 93, Legs 67), and the board has been unable to explain the underweighting of legs.

**Torso: Hold.** *Bench Press* is the index fund of the portfolio: up 7%, low volatility, and range-bound around 95–100 kg since mid-2025. Nobody gets excited about it, but nobody sells it either. *Pull-Up* broke out to an all-time high in September on strong added-weight fundamentals; momentum traders are piling in. *Cable Row* (+11%) briefly went dark in summer 2025, a trading halt the company blamed on "the beach". *Incline DB Press* peaked in April 2025 and has traded sideways ever since, like a utility stock that's given up on growth.

**Arms: Buy.** The shoulder sector is the clear winner: *Shoulder DB Press* (+24%) and *Lateral Raise* (+30%) both closed at highs. *Skull Crusher* had a textbook IPO, opening at 40 and collapsing to 27 within months before clawing its way back to 38. Early investors want a word. *Tricep Extension* is up 83%, though it listed near its lows in August 2025, the same month *Tricep Pushdown* was delisted. The SEC is looking into the timing. *Cable Curl* (−10%) peaked in early 2025 and is the portfolio's quiet underperformer; management says it's "focused on long-term value", i.e. nothing. *Dips* and *Barbell Curl* have been delisted. Shareholders were not consulted.

**Legs: Sell.** The sector has been in a bear market since July 2025. *Squat* (−7%) and *Romanian Deadlift* (−8%) both peaked that summer and have been consolidating at lower levels for over a year, which is a polite way of saying they gave up. The exception is *Calf Raise*, up 213%, a gain the auditors have traced to a switch from dumbbells to a machine. Technically legal. *Leg Raise* is a machine and trades accordingly.

**Watchlist.** *Push-Up* listed in August 2026 and went straight up on light volume, classic meme-stock behaviour. *Overhead Press* traded once and was never seen again.

## Notes to future me

- Log workouts in `data/Workout log YYYY.txt`. The format is in [parsing-info.md](parsing-info.md).
- Run `python parse.py`, then commit and push `data.js`. The site updates by itself a minute later.
- `parse.py` complains about lines it can't read. Listen to it.
- Bodyweight is hardcoded at 78 kg, approximately, and selectively measured.
- Exercises logged fewer than 8 times don't get a chart. Overhead press, I saw what you did.
