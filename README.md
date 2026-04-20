# Noah Stephenson — Personal Portfolio

Personal resume and portfolio website for Noah Stephenson, Systems Engineering Cadet at West Point (USMA).

Built with [Pelican](https://getpelican.com/) (Python static site generator), a custom HTML/CSS theme, and deployed on Render.

---

## Local Setup

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
source venv/Scripts/activate   # Windows (Git Bash)
# or: source venv/bin/activate  # macOS / Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the development server**
```bash
pelican --autoreload --listen
```
Visit [http://localhost:8000](http://localhost:8000)

---

## Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/your-repo.git
git push -u origin main
```

---

## Deploy on Render

1. Push the repository to GitHub
2. Log in to [Render](https://render.com) → **New** → **Static Site**
3. Connect your GitHub repository
4. Configure:
   - **Build Command**: `pip install -r requirements.txt && pelican content -o output -s pelicanconf.py`
   - **Publish Directory**: `output`
5. Click **Deploy Site**

After your first successful deploy, update `SITEURL` in `publishconf.py` with your Render URL (e.g. `https://noahstephenson.onrender.com`).
