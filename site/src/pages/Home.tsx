export default function Home() {
  return (
    <section className="container">
      <div className="panel" style={{padding: 24}}>
        <h1 style={{marginTop: 0}}>Moonlander Optimal Control</h1>
        <p>This site highlights the scientific findings and methodology behind our optimal control study of a 2D lunar lander.</p>
        <h2>Navigate</h2>
        <ul>
          <li>Findings: concise takeaways and key results, with links to supporting figures → <a href="#/findings">Findings</a></li>
          <li>Methods: the mathematical formulation, assumptions, and numerical approach → <a href="#/methodology">Methodology</a></li>
          <li>Results: curated plots and visuals illustrating trajectories and controls → <a href="#/results">Results</a></li>
          <li>Authors: contributors credited as listed in the LaTeX sources → <a href="#/authors">Authors</a></li>
          <li>Notebooks: curated notebooks list → <a href="#/notebooks">Notebooks</a></li>
          <li>Quickstart: optional instructions to run code → <a href="#/quickstart">Quickstart</a></li>
        </ul>
        <p>If you do want to run the code, see Quickstart.</p>
      </div>
    </section>
  )
}

