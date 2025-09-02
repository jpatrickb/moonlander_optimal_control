export default function Home() {
  return (
    <section className="container">
      <div className="panel" style={{padding: 24}}>
        <h1 style={{marginTop: 0}}>Moonlander Optimal Control</h1>
        <p>This site highlights the scientific findings and methodology behind our optimal control study of a 2D lunar lander.</p>
        <h2>Navigate</h2>
        <ul>
          <li><a href="#/findings"><u>Findings</u></a>: concise takeaways and key results, with links to supporting figures</li>
          <li><a href="#/methodology"><u>Methodology</u></a>: the mathematical formulation, assumptions, and numerical approach</li>
          <li><a href="#/results"><u>Results</u></a>: curated plots and visuals illustrating trajectories and controls</li>
          <li><a href="#/authors"><u>Authors</u></a>: contributors credited as listed in the LaTeX sources</li>
          <li><a href="#/notebooks"><u>Notebooks</u></a>: curated notebooks list</li>
          <li><a href="#/quickstart"><u>Quickstart</u></a>: optional instructions to run code</li>
        </ul>
      </div>
    </section>
  )
}

