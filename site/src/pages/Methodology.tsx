export default function Methodology() {
  return (
    <section className="container">
      <div className="panel" style={{padding: 24}}>
        <h1 style={{marginTop:0}}>Methodology</h1>
        <p>This section outlines the optimal control formulation and numerical approach.</p>
        <h2>Problem setup (high-level)</h2>
        <ul>
          <li>State: <Math>(x, y, \dot{x}, \dot{y})</Math></li>
          <li>Control: <Math>(u_x, u_y)</Math> (thrust components)</li>
          <li>
            Dynamics:
            <Math display>{`\\dot{x} = \\dot{x},\\ \quad \\dot{y} = \\dot{y},\\ \quad \\ddot{x} = u_x,\\ \quad \\ddot{y} = u_y - g`}</Math>
          </li>
          <li>Objective: weighted combination of control effort and terminal time/velocity</li>
          <li>Constraints: fixed initial state; terminal vertical position to ground; costate/Hamiltonian terminal conditions</li>
        </ul>
        <h2>Numerical method</h2>
        <ul>
          <li>Derive costate dynamics via Pontryagin’s Minimum Principle</li>
          <li>Solve two-point boundary value problem with SciPy <code>solve_bvp</code></li>
          <li>Time normalization with parameterized final time</li>
          <li>Compute controls from costates</li>
        </ul>
        <p>See <code>lunar.py</code> and <code>utils.py</code> for working implementations. Obstacle variants are in <code>multi_obstacle.py</code>.</p>
      </div>
    </section>
  )
}

