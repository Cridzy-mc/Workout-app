# Cut Camp

An iPhone workout + calorie tracker with a built-in 4-week fat-loss program.

- **Today**: "next up" action, today's workout with a live 3D demo, calories/protein ring, steps, water, weight, daily habits.
- **Train**: week view, 3D previews of every exercise, step-by-step workout player (big buttons, weight/rep steppers, auto rest timer, countdown timers, screen kept awake), custom workouts, weekly schedule.
- **Food**: search with portions, recent foods, copy yesterday, and (inside Claude) AI logging from a sentence or a photo.
- **Coach**: daily game plan, weekly insights, habits, and (inside Claude) an AI coach that can log food/weight/steps, build workouts, change the schedule and adjust calories.
- **Progress**: weight trend (7-day average), realistic timeline, stats, backup and restore.

3D figures use three.js (bundled in `vendor/` for offline use).

Calorie and protein targets come from the Mifflin-St Jeor formula with a 500–1000 kcal deficit, never below a safe floor.

## Install on iPhone

1. In GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch**, pick this branch and `/ (root)`, then Save.
2. After a minute, open `https://<your-username>.github.io/workout-app/` in **Safari** on your iPhone.
3. Tap **Share → Add to Home Screen**. It opens full screen like a normal app and works offline.

Data is stored on the phone. Use **Progress → Copy backup** now and then.

## Editing

The app lives in `src/app.html`. Run `./scripts/build.sh` to regenerate `index.html`.
