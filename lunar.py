"""
Deprecated module.

This file is kept as a thin shim to preserve imports like `from lunar import LunarLander`.
Please import from the package instead:

    from moonlander_optimal_control import LunarLander

"""
from __future__ import annotations

import warnings

warnings.warn(
    "lunar.py is deprecated. Import from moonlander_optimal_control instead:",
    DeprecationWarning,
    stacklevel=2,
)

try:
    from moonlander_optimal_control import LunarLander  # re-export
except Exception as e:  # pragma: no cover
    # Provide a friendly error if the package is not importable
    raise ImportError(
        "Could not import LunarLander from moonlander_optimal_control. "
        "Ensure 'src' is on sys.path or install the package in your environment."
    ) from e


if __name__ == "__main__":  # simple demo
    # Minimal example to mirror previous behavior
    lander = LunarLander([5, 10], 1.0)
    lander.find_path()
    lander.plot_state_controls()
