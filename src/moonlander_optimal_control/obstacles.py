# Thin obstacle API wrappers around multi_obstacle.py

# Re-export core helpers for convenience
try:
    from multi_obstacle import (
        moving_obstacle,
        moving_obstacle_dx,
        moving_obstacle_dy,
        avoid_many_moving_obstacle,
    )
except Exception:  # pragma: no cover - allow import even if optional deps missing
    moving_obstacle = None
    moving_obstacle_dx = None
    moving_obstacle_dy = None
    avoid_many_moving_obstacle = None

__all__ = [
    "moving_obstacle",
    "moving_obstacle_dx",
    "moving_obstacle_dy",
    "avoid_many_moving_obstacle",
]

