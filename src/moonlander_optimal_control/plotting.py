from typing import Iterable, Optional, Tuple

import numpy as np
import matplotlib.pyplot as plt


def plot_summary(t, x, y, xp, yp, ux, uy, tf):
    plt.style.use('dark_background')
    print("Final Time:", tf)
    print("Final Position:", (np.round(x[-1], 3), np.round(y[-1], 3)))

    plt.figure(figsize=(12, 18))

    plt.subplot(421)
    plt.plot(t, x)
    plt.title("x Position")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Position (meters)")

    plt.subplot(422)
    plt.plot(t, y)
    plt.title("y Position")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Position (meters)")

    plt.subplot(423)
    plt.plot(t, xp)
    plt.title("Velocity $V_x$")
    plt.xlabel("Time (seconds)")
    plt.ylabel(r"Velocity ($\\frac{m}{s}$)")

    plt.subplot(424)
    plt.plot(t, yp)
    plt.title("Velocity $V_y$")
    plt.xlabel("Time (seconds)")
    plt.ylabel(r"Velocity ($\\frac{m}{s}$)")

    plt.subplot(425)
    plt.plot(t, ux)
    plt.title("Control $U_x$")
    plt.xlabel("Time (seconds)")
    plt.ylabel(r"Acceleration ($\\frac{m}{s^2}$)")

    plt.subplot(426)
    plt.plot(t, uy)
    plt.title("Control $U_y$")
    plt.xlabel("Time (seconds)")
    plt.ylabel(r"Acceleration ($\\frac{m}{s^2}$)")

    plt.subplot(427)
    plt.plot(t, np.arctan2(-ux, uy))
    plt.title(r"Lander Angle ($\\theta$)")
    plt.yticks([-np.pi/2, -np.pi/4, 0, np.pi / 4, np.pi/2], [r"$-\\frac{\\pi}{2}$", r"$-\\frac{\\pi}{4}$", "0", r"$\\frac{\\pi}{4}$", r"$\\frac{\\pi}{2}$"])
    plt.xlabel("Time (seconds)")
    plt.ylabel("Angle (radians)")

    plt.subplot(428)
    plt.plot(t, (ux**2 + uy**2)**0.5)
    plt.title(r"Thrust Magnitude ($\\tau$)")
    plt.xlabel("Time (seconds)")
    plt.ylabel(r"Magnitude ($\\frac{m}{s^2}$)")

    plt.tight_layout()


def plot_controls(t, ux, uy):
    plt.style.use('dark_background')
    plt.subplot(211)
    plt.plot(t, np.arctan2(-ux, uy))
    plt.title(r"Lander Angle ($\\theta$)")
    plt.yticks([0, np.pi / 8, np.pi / 4, 3 * np.pi / 8], ["0", r"$\\frac{\\pi}{8}$", r"$\\frac{\\pi}{4}$", r"$\\frac{3\\pi}{8}$"])  # noqa: E501
    plt.xlabel("Time (seconds)")
    plt.ylabel("Angle (radians)")

    plt.subplot(212)
    plt.plot(t, (ux**2 + uy**2)**0.5)
    plt.title(r"Acceleration Magnitude ($\\tau$)")
    plt.xlabel("Time (seconds)")
    plt.ylabel(r"Magnitude ($m/s^2$)")

    plt.tight_layout()


def plot_trajectory(
    x,
    y,
    obstacles: Optional[Iterable] = None,
    xlim: Optional[Tuple[float, float]] = None,
    guess: Optional[Tuple] = None,
    save_file: Optional[str] = None,
):
    plt.style.use('dark_background')

    if obstacles is not None:
        for obstacle in obstacles:
            x_vals = np.linspace(-10.0, 10.0, 150)
            y_vals = np.linspace(-10.0, 10.0, 150)
            X, Y = np.meshgrid(x_vals, y_vals)
            Z = obstacle.obstacle(X, Y)
            plt.contour(X, Y, Z, linewidths=5, cmap='Greys')

    if guess is not None:
        guess_x, guess_y = guess
        plt.plot(guess_x, guess_y, label="Initial Guess")

    plt.plot(x, y, color='#8dd3c7', label="Optimal Trajectory")

    if guess is not None:
        plt.legend()

    plt.title("Lander Trajectory")

    if xlim is not None:
        plt.xlim(*xlim)
    plt.ylim(0, np.max(y) + 0.5)
    plt.xlabel("Horizontal Position (meters)")
    plt.ylabel("Vertical Position (meters)")

    plt.tight_layout()

    if save_file is not None:
        plt.savefig(save_file, dpi=300)

    plt.show()

