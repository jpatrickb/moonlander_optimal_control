# Quickstart

## 1) Install dependencies

```bash path=null start=null
python -m venv .venv
source .venv/bin/activate  # on macOS/Linux
pip install -r requirements.txt
```

To preview the documentation locally:

```bash path=null start=null
pip install -r docs/requirements-docs.txt
mkdocs serve
```

## 2) Run a baseline solve and plots
Using the current functional API in `utils.py`:

```python path=null start=null
from utils import lunar_lander, make_plots

pos = (5.0, 10.0)
vx0 = 1.0

# Solve the BVP and compute controls
t, x, y, xp, yp, ux, uy, tf = lunar_lander(pos, vx0, t_steps=400)

# Plot summary figures
make_plots(t, x, y, xp, yp, ux, uy, tf)
```

Or, using the new package API (preferred):

```python path=null start=null
from moonlander_optimal_control import solve_baseline, plot_summary

t, x, y, xp, yp, ux, uy, tf = solve_baseline((5.0, 10.0), 1.0, t_steps=400)
plot_summary(t, x, y, xp, yp, ux, uy, tf)
```

## 3) Build the docs site (optional)

```bash path=null start=null
mkdocs build
```

This generates a static site in `site/` (ignored by git). GitHub Actions can deploy this to GitHub Pages automatically later.

