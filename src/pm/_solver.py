"""Shared cvxpy solve guard.

Private helper: every optimizer in this repo returns weights from
`cp.Variable.value`, which is `None` when the solver doesn't reach an
optimal point (infeasible, unbounded, or solver error). Without a check,
`np.asarray(None).ravel()` yields `array([None], dtype=object)` - no
exception, and the bad value silently poisons whatever consumes it.
"""
import numpy as np

_ACCEPTABLE = ("optimal", "optimal_inaccurate")


def solved_weights(problem, variable):
    """Solve `problem` and return `variable`'s value as a float array.

    Raises ValueError with the solver status if no optimal point was
    reached, rather than returning an object-dtype array of None.
    """
    problem.solve()
    if problem.status not in _ACCEPTABLE or variable.value is None:
        raise ValueError(
            f"Optimization did not reach an optimal solution (solver status: "
            f"{problem.status!r}). Check that the constraints are feasible - "
            f"e.g. a long-only portfolio needs max_weight >= 1/n_assets to sum to 1."
        )
    return np.asarray(variable.value, dtype=float).ravel()
