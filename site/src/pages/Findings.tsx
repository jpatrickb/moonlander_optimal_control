export default function Findings() {
  return (
    <section className="container">
      <div className="panel" style={{padding: 24}}>
        <h1 style={{marginTop:0}}>Key Findings</h1>
        <p>This page highlights the scientific takeaways from our optimal control study of a 2D lunar lander. It is intentionally concise and links to supporting visuals on the Results page.</p>
        <h2>Headline results</h2>
        <ul>
          <li>The baseline optimal control policy produces smooth thrust profiles that meet terminal constraints with minimal effort.</li>
          <li>Final-time appears sensitive to initial horizontal velocity; energy use increases with larger |v_x(0)|.</li>
          <li>The cost functional J balances control effort with terminal conditions; emphasis on terminal velocity yields softer touchdowns at the expense of higher thrust.</li>
        </ul>
        <p>See the Results page for figures referenced here.</p>
        <h2>Context from the model</h2>
        <ul>
          <li>State: (x, y, x_dot, y_dot)</li>
          <li>Control: (u_x, u_y)</li>
          <li>Gravity: constant downward acceleration</li>
          <li>Objective: minimize control effort plus penalties on terminal time/velocity</li>
        </ul>
        <p>For a more complete mathematical formulation and numerical approach, see Methods.</p>
        <h2>Highlights from results</h2>
        <ul>
          <li>Baseline trajectory and control profiles illustrate qualitatively stable descents under gravity with targeted thrusting.</li>
          <li>Composite panels summarize state and control evolution.</li>
        </ul>
        <h3>Suggested next additions</h3>
        <ul>
          <li>Side-by-side comparisons for different initial conditions</li>
          <li>Sensitivity to cost weights (alpha, beta, gamma)</li>
          <li>Obstacle-avoidance trials and outcomes</li>
        </ul>
      </div>
    </section>
  )
}

