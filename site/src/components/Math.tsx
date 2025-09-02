import katex from 'katex'
import { useMemo } from 'react'

type MathProps = {
  children: string
  display?: boolean
}

export function Math({ children, display = false }: MathProps) {
  const html = useMemo(() => {
    try {
      return katex.renderToString(children, { displayMode: display, throwOnError: false, output: 'html' })
    } catch {
      return children
    }
  }, [children, display])

  if (display) {
    return <div className="katex-display" dangerouslySetInnerHTML={{ __html: html }} />
  }
  return <span className="katex" dangerouslySetInnerHTML={{ __html: html }} />
}

