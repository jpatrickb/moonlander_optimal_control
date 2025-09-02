export default function Quickstart() {
  return (
    <section className="container">
      <div className="panel" style={{padding: 24}}>
        <h1 style={{marginTop:0}}>Quickstart</h1>
        <h2>1) Install dependencies</h2>
        <pre><code>python -m venv .venv
source .venv/bin/activate  # on macOS/Linux
pip install -r requirements.txt</code></pre>
        <h2>2) Run a baseline solve and plots</h2>
        <p>Using the current functional API in <code>utils.py</code>:</p>
        <pre><code>from utils import lunar_lander, make_plots

pos = (5.0, 10.0)
vx0 = 1.0

# Solve the BVP and compute controls
t, x, y, xp, yp, ux, uy, tf = lunar_lander(pos, vx0, t_steps=400)

# Plot summary figures
make_plots(t, x, y, xp, yp, ux, uy, tf)</code></pre>
        <p>Or, using the new package API (preferred):</p>
        <pre><code>from moonlander_optimal_control import solve_baseline, plot_summary

t, x, y, xp, yp, ux, uy, tf = solve_baseline((5.0, 10.0), 1.0, t_steps=400)
plot_summary(t, x, y, xp, yp, ux, uy, tf)</code></pre>
      </div>
    </section>
  )
}

