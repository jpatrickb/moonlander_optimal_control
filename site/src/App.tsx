import { Routes, Route, Navigate, NavLink } from 'react-router-dom'
import './App.css'
import Home from './pages/Home'
import Findings from './pages/Findings.mdx'
import Methodology from './pages/Methodology.mdx'
import Results from './pages/Results'
import Notebooks from './pages/Notebooks'
import Authors from './pages/Authors'

function App() {
  return (
    <div className="app-root">
      <header className="navbar">
        <div className="navbar-inner">
<a className="brand brand-title" href="https://github.com/jpatrickb/moonlander_optimal_control" target="_blank" rel="noreferrer">Fly Me To The Moon!</a>
          <nav className="nav-links">
            <NavLink to="/" className={({isActive}) => `nav-link ${isActive ? 'active' : ''}`}>Home</NavLink>
            <NavLink to="/findings" className={({isActive}) => `nav-link ${isActive ? 'active' : ''}`}>Findings</NavLink>
            <NavLink to="/methodology" className={({isActive}) => `nav-link ${isActive ? 'active' : ''}`}>Methodology</NavLink>
            <NavLink to="/results" className={({isActive}) => `nav-link ${isActive ? 'active' : ''}`}>Results</NavLink>
            <NavLink to="/notebooks" className={({isActive}) => `nav-link ${isActive ? 'active' : ''}`}>Notebooks</NavLink>
            <NavLink to="/authors" className={({isActive}) => `nav-link ${isActive ? 'active' : ''}`}>Authors</NavLink>
          </nav>
        </div>
      </header>
      <main className="container">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/findings" element={<Findings />} />
          <Route path="/methodology" element={<Methodology />} />
          <Route path="/results" element={<Results />} />
          <Route path="/notebooks" element={<Notebooks />} />
          <Route path="/authors" element={<Authors />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </main>
      <footer className="footer container">© {new Date().getFullYear()} Fly Me To The Moon!</footer>
    </div>
  )
}

export default App
