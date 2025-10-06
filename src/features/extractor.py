import numpy as np
from scipy.stats import skew, kurtosis

def _extract_tsp_features(instance):
    """Calculates a set of numerical features for a TSP instance."""
    features = {}
    
    # --- THE FIX IS HERE ---
    # The size is the number of cities, which is the dimension of the distance matrix.
    features['instance_size'] = len(instance['distance_matrix'])
    
    distances = np.array(instance['distance_matrix'])
    
    # Flatten the upper triangle of the distance matrix to avoid duplicates and zeros
    upper_triangle = distances[np.triu_indices(len(distances), k=1)]
    
    # Category B: Statistical Features
    features['data_mean'] = np.mean(upper_triangle)
    features['data_std_dev'] = np.std(upper_triangle)
    features['data_skewness'] = skew(upper_triangle)
    features['data_kurtosis'] = kurtosis(upper_triangle)
    features['data_min'] = np.min(upper_triangle)
    features['data_max'] = np.max(upper_triangle)
    features['data_q1'] = np.percentile(upper_triangle, 25)
    features['data_q3'] = np.percentile(upper_triangle, 75)
    
    return features

def _extract_kp_features(instance):
    """Calculates a set of numerical features for a Knapsack Problem instance."""
    # This is a placeholder. You would add real feature calculations here.
    features = {}
    features['instance_size'] = len(instance['values'])
    return features

def extract_features(instance, problem_type):
    """Master function to extract features from a problem instance."""
    if problem_type == 'TSP':
        return _extract_tsp_features(instance)
    elif problem_type == 'KP':
        return _extract_kp_features(instance)
    # Add elif for JSSP here if needed
    else:
        raise ValueError("Unknown problem type specified.")

