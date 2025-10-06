import random
from simanneal import Annealer
import numpy as np

class TspAnnealer(Annealer):
    """
    Custom Annealer for the Traveling Salesperson Problem.
    """
    def __init__(self, state, distance_matrix):
        self.distance_matrix = distance_matrix
        super(TspAnnealer, self).__init__(state)

    def move(self):
        """Swaps two cities in the route."""
        a = random.randint(0, len(self.state) - 1)
        b = random.randint(0, len(self.state) - 1)
        self.state[a], self.state[b] = self.state[b], self.state[a]

    def energy(self):
        """Calculates the total length of the tour."""
        e = 0
        for i in range(len(self.state)):
            e += self.distance_matrix[self.state[i-1]][self.state[i]]
        return e

def solve_tsp_with_sa(problem_instance):
    """
    Solves a Traveling Salesperson Problem instance using Simulated Annealing.
    """
    dist_matrix = problem_instance["distance_matrix"]
    n_cities = len(dist_matrix)
    
    # Initial random tour
    initial_state = list(range(n_cities))
    random.shuffle(initial_state)

    tsp_annealer = TspAnnealer(initial_state, dist_matrix)
    
    # Tune annealing parameters
    tsp_annealer.set_schedule(tsp_annealer.auto(minutes=0.1))

    best_state, best_energy = tsp_annealer.anneal()

    return best_state, best_energy
