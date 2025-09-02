export default function Home() {
  return (
    <section className="container">
      <div className="panel" style={{padding: 24}}>
        <h1 className="site-title" style={{marginTop: 0}}>Fly Me To The Moon!</h1>
        <p>This site highlights the scientific findings and methodology behind our optimal control study of a 2D lunar lander.</p>

        <div className="card" style={{marginTop:12}}>
          <strong>Final Poster (PDF): </strong>
          <a href="/moonlander_optimal_control/assets/FlyMeToTheMoonPoster.pdf" target="_blank" rel="noreferrer">FlyMeToTheMoonPoster.pdf ↗</a>
        </div>

        <h2 style={{marginTop:18}}>Navigate</h2>
        <ul>
          <li><a href="#/findings">Findings</a> — concise takeaways and key results, with links to supporting figures</li>
          <li><a href="#/methodology">Methodology</a> — the mathematical formulation, assumptions, and numerical approach</li>
          <li><a href="#/results">Results</a> — curated plots and visuals illustrating trajectories and controls</li>
          <li><a href="#/authors">Authors</a> — contributors credited as listed in the LaTeX sources</li>
          <li><a href="#/notebooks">Notebooks</a> — curated notebooks list</li>
        </ul>
      </div>
    </section>
  )
}

