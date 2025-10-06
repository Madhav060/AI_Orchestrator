from ortools.algorithms import pywrapknapsack_solver

def solve_kp_with_bb(problem_instance):
    """
    Solves a 0/1 Knapsack Problem instance using the OR-Tools Branch and Bound solver.
    """
    values = problem_instance["values"]
    weights = [problem_instance["weights"]]  # OR-Tools expects a list of lists
    capacities = [problem_instance["capacity"]]

    # Create the solver instance (using the Branch and Bound algorithm)
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
        "KnapsackExample"
    )

    # Initialize and solve
    solver.Init(values, weights, capacities)
    computed_value = solver.Solve()

    # Extract packed items
    packed_items = [i for i in range(len(values)) if solver.BestSolutionContains(i)]

    return packed_items, computed_value
