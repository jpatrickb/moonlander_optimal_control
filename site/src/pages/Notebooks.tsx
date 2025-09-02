export default function Notebooks() {
  return (
    <section className="container">
      <div className="panel" style={{padding: 24}}>
        <h1 style={{marginTop:0}}>Notebooks</h1>
        <p>Notebooks are organized under the <code>notebooks/</code> directory.</p>
        <h2>Curated set</h2>
        <ul>
          <li><code>notebooks/starter_code.ipynb</code> — baseline setup</li>
          <li><code>notebooks/visualization.ipynb</code> — plotting and trajectory visuals</li>
          <li><code>notebooks/landing_pos_with_cost.ipynb</code> — objective and terminal conditions</li>
          <li><code>notebooks/obstacle_avoidance.ipynb</code> — obstacle variants</li>
        </ul>
        <h2>Exploratory notebooks (archived)</h2>
        <ul>
          <li><code>notebooks/9x_experiments/adam_experimenting.ipynb</code></li>
          <li><code>notebooks/9x_experiments/tiara_experimenting.ipynb</code></li>
          <li><code>notebooks/9x_experiments/tj_experimenting.ipynb</code></li>
          <li><code>notebooks/9x_experiments/patrick_messing_around.ipynb</code></li>
          <li><code>notebooks/9x_experiments/angle_enforcement.ipynb</code></li>
          <li><code>notebooks/9x_experiments/landing_zones.ipynb</code></li>
        </ul>
        <p>Tip: Use nbviewer for a fast read-only view if GitHub rendering is slow.</p>
      </div>
    </section>
  )
}

