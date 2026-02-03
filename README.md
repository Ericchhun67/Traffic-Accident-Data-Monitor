# Traffic & Accident Data Monitor

Flask-powered Traffic & Accident Data Monitor that visualizes live traffic flow, accident trends, and city stats. Uses Python for analytics, Leaflet.js for maps, and modular handlers for real-time updates. Showcases backend data pipelines, frontend visualization, and simulation systems.

## Live Links
- **Landing Page (GitHub Pages)**: `https://ericchhun67.github.io/Traffic-Accident-Data-Monitor/` (enable Pages for the `/docs` folder)
- **Live Flask App**: add your hosted URL here once deployed

## Local Development
```bash
python app.py
```
Then open `http://127.0.0.1:5002` (or the port printed in your terminal).

## GitHub Pages Landing Page
This repo includes a static landing page in `docs/` for GitHub Pages.

Enable it:
1. Go to **Repo Settings → Pages**
2. Set **Branch** to `main` and **Folder** to `/docs`
3. Save — your landing page will appear at the URL above

## Flask Hosting
This repo includes a `render.yaml` for one-click deployment on Render.\n\nSteps:\n1. Go to Render → New → Blueprint\n2. Select this repo\n3. Render will detect `render.yaml` and deploy the web service\n4. Once live, update the landing page links in `docs/index.html` to point to the Render URL
