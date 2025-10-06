import time
from typing import Dict, Any, Tuple

# --- THE FIX IS HERE ---
# Add a '.' before each local import to make it relative.
from .solvers import cp_sat_solver
from .solvers import branch_and_bound_solver
from .solvers import genetic_algorithm_solver
from .solvers import simulated_annealing_solver


def solve(problem_instance: Dict[str, Any], algorithm_name: str) -> Tuple:
    """
    Master function to solve a given problem instance with a specified algorithm.
    This acts as a universal remote, dispatching the call to the correct specialized solver.

    Args:
        problem_instance: A dictionary containing all problem data (e.g., cities, items, capacity).
        algorithm_name: A string specifying the algorithm ('GA', 'SA', 'B&B', 'CP-SAT').

    Returns:
        A tuple of (solution, performance_metrics).
        - solution: The final solution found by the algorithm (e.g., a tour list, packed items list).
        - performance_metrics: A dictionary containing 'runtime' and 'objective_value'.
    """
    start_time = time.time()
    
    problem_type = problem_instance.get("type")
    if not problem_type:
        raise ValueError("Problem instance must have a 'type' key (e.g., 'TSP', 'KP').")

    solution = None
    objective_value = float('inf')

    if problem_type == 'KP':
        if algorithm_name == 'B&B':
            solution, objective_value = branch_and_bound_solver.solve_knapsack_with_bnb(problem_instance)
        else:
            raise ValueError(f"Algorithm '{algorithm_name}' is not supported for KP.")
            
    elif problem_type == 'TSP':
        if algorithm_name == 'SA':
            solution, objective_value = simulated_annealing_solver.solve_tsp_with_sa(problem_instance)
        elif algorithm_name == 'GA':
            solution, objective_value = genetic_algorithm_solver.solve_tsp_with_ga(problem_instance)
        else:
            raise ValueError(f"Algorithm '{algorithm_name}' is not supported for TSP.")
            
    else:
        raise ValueError(f"Unknown problem type: {problem_type}")

    end_time = time.time()
    runtime = end_time - start_time
    
    metrics = {
        "runtime": runtime,
        "objective_value": objective_value
    }
    
    return solution, metrics
