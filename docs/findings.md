# Key Findings

This page highlights the scientific takeaways from our optimal control study of a 2D lunar lander. It is intentionally concise and links to supporting visuals on the Results page.

## Headline results
- The baseline optimal control policy produces smooth thrust profiles that meet terminal constraints with minimal effort.
- Final-time appears sensitive to initial horizontal velocity; energy use increases with larger |v_x(0)|.
- The cost functional J balances control effort with terminal conditions; emphasis on terminal velocity yields softer touchdowns at the expense of higher thrust.

See the Results page for figures referenced here.

## Context from the model
- State: (x, y, x_dot, y_dot)
- Control: (u_x, u_y)
- Gravity: constant downward acceleration
- Objective: minimize control effort plus penalties on terminal time/velocity

For a more complete mathematical formulation and numerical approach, see Methods.

## Highlights from results
- Baseline trajectory and control profiles illustrate qualitatively stable descents under gravity with targeted thrusting.
- Composite panels summarize state and control evolution.

Suggested next additions:
- Side-by-side comparisons for different initial conditions
- Sensitivity to cost weights (alpha, beta, gamma)
- Obstacle-avoidance trials and outcomes
