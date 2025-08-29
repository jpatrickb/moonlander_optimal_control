from typing import Tuple

import numpy as np
from scipy.integrate import solve_bvp


def solve_baseline(
    pos: Tuple[float, float],
    vx0: float,
    t_steps: int = 200,
    tf_guess: float = 20.0,
    y0_guess: float = 1.0,
    alpha: float = 10.0,
    beta: float = 25.0,
    gamma: float = 3.0,
    nu: float = 0.0,
    G: float = 2.0,
):
    """Solve the baseline lunar lander BVP.

    Returns: t, x, y, xp, yp, ux, uy, tf
    """
    x_init, y_init = pos

    def ode(t, y, p):
        tf = p[0]
        return tf * np.array(
            [
                y[2],
                y[3],
                y[6] / (2 * alpha),
                y[7] / (2 * alpha) - G,
                np.zeros_like(y[0]),
                nu * (1 - np.heaviside(y[1], 0)),
                -y[4],
                -y[5],
            ]
        )

    def bc(ya, yb, p):
        uxf = yb[6] / (2 * alpha)
        uyf = yb[7] / (2 * alpha)
        return np.array(
            [
                ya[0] - x_init,
                ya[1] - y_init,
                ya[2] - vx0,
                ya[3],
                yb[1],
                yb[4],
                yb[6] - 2 * beta * yb[2],
                yb[7] - 2 * beta * yb[3],
                yb[4] * yb[2]
                + yb[5] * yb[3]
                + yb[6] * uxf
                + yb[7] * (uyf - G)
                - alpha * (uxf**2 + uyf**2)
                - gamma
                + nu * (np.minimum(0, yb[1])),
            ]
        )

    tf_0 = tf_guess
    t_eval = np.linspace(0, 1, t_steps)
    y0 = y0_guess * np.ones((8, t_steps))
    y0[0] = np.ones((1, t_steps))

    y0[0] *= x_init
    y0[1] = np.linspace(y_init, 0, t_steps)
    y0[2] = np.linspace(vx0, 0, t_steps)

    sol = solve_bvp(ode, bc, t_eval, y0, p=np.array([tf_0]), max_nodes=30000)
    tf = sol.p[0]

    x = sol.y[0]
    y = sol.y[1]
    xp = sol.y[2]
    yp = sol.y[3]
    ux = sol.y[6] / (2 * alpha)
    uy = sol.y[7] / (2 * alpha)
    t_vals = sol.x * tf

    return t_vals, x, y, xp, yp, ux, uy - G, tf


def solve_with_final_angle(
    pos: Tuple[float, float],
    vx0: float,
    t_steps: int = 200,
    tf_guess: float = 20.0,
    y0_guess: float = 1.0,
    alpha: float = 10.0,
    beta: float = 25.0,
    gamma: float = 3.0,
    nu: float = 0.0,
    G: float = 2.0,
    rho: float = 0.01,
    final_angle_on: bool = True,
):
    """Solve the lunar lander BVP with an extra final-angle penalty term.

    Returns: t, x, y, xp, yp, ux, uy, tf
    """
    x_init, y_init = pos

    def ode(t, y, p):
        tf = p[0]
        return tf * np.array(
            [
                y[2],
                y[3],
                y[6] / (2 * alpha),
                y[7] / (2 * alpha) - G,
                np.zeros_like(y[0]),
                nu * (1 - np.heaviside(y[1], 0))
                + (
                    final_angle_on * 2 * ((y[6] / (2 * alpha)) ** 2) / (y[1] + rho) ** 3
                ),
                -y[4],
                -y[5],
            ]
        )

    def bc(ya, yb, p):
        uxf = yb[6] / (2 * alpha)
        uyf = yb[7] / (2 * alpha)
        return np.array(
            [
                ya[0] - x_init,
                ya[1] - y_init,
                ya[2] - vx0,
                ya[3],
                yb[1],
                yb[4],
                yb[6] - 2 * beta * yb[2],
                yb[7] - 2 * beta * yb[3],
                yb[4] * yb[2]
                + yb[5] * yb[3]
                + yb[6] * uxf
                + yb[7] * (uyf - G)
                - alpha * (uxf**2 + uyf**2)
                - gamma
                + nu * (np.minimum(0, yb[1]))
                - (final_angle_on * (uxf / (yb[1] + rho)) ** 2),
            ]
        )

    tf_0 = tf_guess
    t_eval = np.linspace(0, 1, t_steps)
    y0 = y0_guess * np.ones((8, t_steps))
    y0[0] = np.ones((1, t_steps))

    y0[0] *= x_init
    y0[1] = np.linspace(y_init, 0, t_steps)
    y0[2] = np.linspace(vx0, 0, t_steps)

    sol = solve_bvp(ode, bc, t_eval, y0, p=np.array([tf_0]), max_nodes=30000)
    tf = sol.p[0]

    x = sol.y[0]
    y = sol.y[1]
    xp = sol.y[2]
    yp = sol.y[3]
    ux = sol.y[6] / (2 * alpha)
    uy = sol.y[7] / (2 * alpha)
    t_vals = sol.x * tf

    return t_vals, x, y, xp, yp, ux, uy - G, tf
