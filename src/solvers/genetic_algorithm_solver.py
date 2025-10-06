import numpy as np
from mealpy import GA, PermutationVar

def solve_tsp_with_ga(problem_instance):
    """
    Solves a Traveling Salesperson Problem instance using a Genetic Algorithm from the mealpy library.
    """
    dist_matrix = np.array(problem_instance["distance_matrix"])
    n_cities = len(dist_matrix)

    def fitness_function(solution):
        """Calculates the total tour length for a given permutation."""
        solution = solution.astype(int)
        tour_length = 0
        for i in range(n_cities):
            u = solution[i]
            v = solution[(i + 1) % n_cities]
            tour_length += dist_matrix[u][v]
        return tour_length

    problem_dict = {
        "obj_func": fitness_function,
        "bounds": PermutationVar(valid_set=list(range(n_cities))),
        "minmax": "min",
    }

    # Configure the Genetic Algorithm
    model = GA.BaseGA(epoch=200, pop_size=100, pc=0.9, pm=0.05)
    
    # --- THE FIX IS HERE ---
    # 1. Get the single "Agent" object returned by the solve function.
    best_agent = model.solve(problem_dict)
    
    # 2. "Unpack" the information from inside the agent object.
    best_position = best_agent.solution
    best_fitness = best_agent.target.objectives[0]

    # The final result should also be clean integers
    return best_position.astype(int).tolist(), best_fitness

