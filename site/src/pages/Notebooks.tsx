const GH = 'https://github.com/jpatrickb/moonlander_optimal_control/blob/main'

export default function Notebooks() {
  return (
    <section className="container">
      <div className="panel" style={{padding: 24}}>
        <h1 style={{marginTop:0}}>Notebooks</h1>
        <p>Notebooks are organized under the <code>notebooks/</code> directory.</p>
        <h2>Curated set</h2>
        <ul>
          <li><a href={`${GH}/notebooks/starter_code.ipynb`} target="_blank" rel="noreferrer"><code>notebooks/starter_code.ipynb</code></a> — baseline setup</li>
          <li><a href={`${GH}/notebooks/visualization.ipynb`} target="_blank" rel="noreferrer"><code>notebooks/visualization.ipynb</code></a> — plotting and trajectory visuals</li>
          <li><a href={`${GH}/notebooks/landing_pos_with_cost.ipynb`} target="_blank" rel="noreferrer"><code>notebooks/landing_pos_with_cost.ipynb</code></a> — objective and terminal conditions</li>
          <li><a href={`${GH}/notebooks/obstacle_avoidance.ipynb`} target="_blank" rel="noreferrer"><code>notebooks/obstacle_avoidance.ipynb</code></a> — obstacle variants</li>
        </ul>
        <h2>Exploratory notebooks (archived)</h2>
        <ul>
          <li><a href={`${GH}/notebooks/9x_experiments/adam_experimenting.ipynb`} target="_blank" rel="noreferrer"><code>notebooks/9x_experiments/adam_experimenting.ipynb</code></a></li>
          <li><a href={`${GH}/notebooks/9x_experiments/tiara_experimenting.ipynb`} target="_blank" rel="noreferrer"><code>notebooks/9x_experiments/tiara_experimenting.ipynb</code></a></li>
          <li><a href={`${GH}/notebooks/9x_experiments/tj_experimenting.ipynb`} target="_blank" rel="noreferrer"><code>notebooks/9x_experiments/tj_experimenting.ipynb</code></a></li>
          <li><a href={`${GH}/notebooks/9x_experiments/patrick_messing_around.ipynb`} target="_blank" rel="noreferrer"><code>notebooks/9x_experiments/patrick_messing_around.ipynb</code></a></li>
          <li><a href={`${GH}/notebooks/9x_experiments/angle_enforcement.ipynb`} target="_blank" rel="noreferrer"><code>notebooks/9x_experiments/angle_enforcement.ipynb</code></a></li>
          <li><a href={`${GH}/notebooks/9x_experiments/landing_zones.ipynb`} target="_blank" rel="noreferrer"><code>notebooks/9x_experiments/landing_zones.ipynb</code></a></li>
        </ul>
      </div>
    </section>
  )
}

