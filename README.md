# Cut Camp

An iPhone workout + calorie tracker with a built-in 4-week fat-loss program.

- **Today**: today's workout, calories and protein left, steps, water, weight.
- **Plan**: this week's calendar, a weekly schedule you can edit, and your realistic timeline.
- **Workouts**: start any workout, log weight/reps per set with a rest timer, create or copy your own workouts.
- **Food**: quick-add common foods, custom foods, meals, recent foods.
- **Progress**: weight trend (7-day average), streaks, stats, backup and restore.

Calorie and protein targets come from the Mifflin-St Jeor formula with a 500–1000 kcal deficit, never below a safe floor.

## Install on iPhone

1. In GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch**, pick this branch and `/ (root)`, then Save.
2. After a minute, open `https://<your-username>.github.io/workout-app/` in **Safari** on your iPhone.
3. Tap **Share → Add to Home Screen**. It opens full screen like a normal app and works offline.

Data is stored on the phone. Use **Progress → Copy backup** now and then.

## Editing

The app lives in `src/app.html`. Run `./scripts/build.sh` to regenerate `index.html`.
