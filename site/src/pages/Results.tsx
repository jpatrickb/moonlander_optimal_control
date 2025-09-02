export default function Results() {
  return (
    <section className="container">
      <div className="panel" style={{padding: 24}}>
        <h1 style={{marginTop:0}}>Results (Gallery)</h1>
        <p>This page showcases a few baseline visuals. More figures and animations will be added over time.</p>

        <h2>Baseline trajectory</h2>
        <img src="/moonlander_optimal_control/assets/trajectory.png" alt="Baseline Trajectory" style={{width:'100%', borderRadius:12, border:'1px solid var(--border)'}} />
        <p>The baseline trajectory shows the lander descending under gravity with optimal thrust to meet terminal conditions.</p>

        <h2>Control summary</h2>
        <img src="/moonlander_optimal_control/assets/control_output.png" alt="Control Summary" style={{width:'100%', borderRadius:12, border:'1px solid var(--border)'}} />
        <p>Control profiles over time (acceleration components, thrust magnitude, and angle) corresponding to the baseline run.</p>

        <h2>Additional visuals</h2>
        <h3>Full output panel</h3>
        <img src="/moonlander_optimal_control/assets/full_output.png" alt="Full Output Panel" style={{width:'100%', borderRadius:12, border:'1px solid var(--border)'}} />
        <p>A composite figure summarizing key states and controls.</p>

        <h3>Gameplay reference</h3>
        <img src="/moonlander_optimal_control/assets/lunar_lander_gameplay.png" alt="Gameplay Reference" style={{width:'100%', borderRadius:12, border:'1px solid var(--border)'}} />
        <p>A reference still from gameplay to contextualize the control problem.</p>

        <h2>Coming soon</h2>
        <ul>
          <li>Obstacle-avoidance trajectories and contours</li>
          <li>Short animations (MP4)</li>
          <li>Additional comparisons across parameter choices</li>
        </ul>
      </div>
    </section>
  )
}

