# Expose a friendly API
from .solver import solve_baseline, solve_with_final_angle
from .plotting import plot_summary, plot_controls, plot_trajectory
from .lunar_lander import LunarLander

__all__ = [
    "solve_baseline",
    "solve_with_final_angle",
    "plot_summary",
    "plot_controls",
    "plot_trajectory",
    "LunarLander",
]

