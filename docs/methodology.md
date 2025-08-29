# Methodology

This section outlines the optimal control formulation and numerical approach.

## Problem setup (high-level)
- State: $(x, y, \dot{x}, \dot{y})$
- Control: $(u_x, u_y)$ (thrust components)
- Dynamics: $\dot{x}=\dot{x},\ \dot{y}=\dot{y},\ \ddot{x}=u_x,\ \ddot{y}=u_y - g$
- Objective: weighted combination of control effort and terminal time/velocity
- Constraints: fixed initial state; terminal vertical position to ground; costate/hamiltonian terminal conditions

## Numerical method
- Derive costate dynamics via Pontryagin’s Minimum Principle
- Solve two-point boundary value problem with SciPy `solve_bvp`
- Time normalization with parameterized final time
- Compute controls from costates

See `lunar.py` and `utils.py` for working implementations. Obstacle variants are in `multi_obstacle.py`.

