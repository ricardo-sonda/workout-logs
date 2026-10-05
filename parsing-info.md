Each entry looks like:

0801 torso
pl 0.9,6,5
bp 80.6/70.7,4
cr 40.12,8,8
dp 28.8,5,5

It has two components:
the header: 0801 torso
0801 is the date in DDMM (so 0801 = 8 January). The year is in the file's name.
the workouts:bp 80.6/70.7,4
The first letters are an abreviation of the workout's name. There is a translation table at the end of this doc. Different exercises from separate splits (so arm day vs torso day) might have the same abreviation, but they are  distinguishable from the particular day.
The second part is composed of "[weight in kg].[number of reps in first set],[number of reps in second set], [and so forth]". So bp 80.6,5 means "bench press 80 kg for 6 reps then for 5 reps".
A "/" means "change of weight". So bp 80.6/70.7,4 means "bench press, 80 kg for 6 reps, then 70 kg for 7 and then 4 reps."
A weight of 0 means that the exercise performed is a body weight exercise and that there are no extra weights attached. I weigh around 78 kg. For bodyweight exercises (pull-ups, dips, push-ups, abs) a weight above 0 is added weight on top of bodyweight.

Known typos the parser tolerates: trailing commas (cr 90.11,9,), stray letters (9,9m), and a "." where a "," was meant (te 22.9/20.9.8 = 20 kg for 9 then 8 reps).
If the same exercise is logged twice on one day, only the first entry is used.

Translation table:
weight number in dumbbell reference the weight of a single dumbbell.
Arm day:
sp = shoulder dumbbell press (typos somewhere reference dp)
sc = skull crusher (typos somewhere refernce sq)
cc = cable curls (bicep cable curs)
bc = barbell curls (free weight, separate from cable curls)
te = tricep cable extension
tp = tricep pushdown (different attachment, separate from tricep extension)
lr = lateral dumbbell raise (typos somewhere reference cr)
di = dips (body weight)
hc = hammer curls
Torso day:
bp = bench press
cr = cable row (sometimes mislabled as cc; a torso cc at 40 kg or more is a cable row)
dp = incline dumbbell press
pl or pu = pullup (body weight. Sets above 0 weight mean added weight).
ps = push ups
cc = cable crunch (for abs)
pd = lat pulldown
cp = incline bench press
oh = overhead press
bl = barbell row
ab = abs (body weight)
pp = cable row on a one-off machine (ignored)
Legs day:
sq = squat
rd = romanian deadlift
cr = calf raises
lr = leg raises (machine)
le = leg extension
cc = cable crunch
hc = hammer curls
