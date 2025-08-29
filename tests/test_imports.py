import importlib


def test_import_package():
    pkg = importlib.import_module("moonlander_optimal_control")
    assert hasattr(pkg, "solve_baseline")
    assert hasattr(pkg, "plot_summary")
    assert hasattr(pkg, "LunarLander")


def test_solver_wrapper_signature():
    pkg = importlib.import_module("moonlander_optimal_control")
    # Ensure it’s callable; do not run the actual solver here (could be slow on CI)
    assert callable(pkg.solve_baseline)

