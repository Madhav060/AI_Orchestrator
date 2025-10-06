# AI Orchestrator Project

This repository contains the source code for the "AI Orchestrator," a meta-learning framework for automated algorithm selection in combinatorial optimization. This codebase corresponds to the completion of Phase 2: Environment Setup and Baseline Implementation.

## Project Structure

The project is organized into the following directories to maintain a clean and modular structure:
/
├── data/
│   └── (raw benchmark datasets will be stored here)
├── notebooks/
│   └── 01_solver_test.ipynb
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── solvers/
│   │   ├── __init__.py
│   │   ├── branch_and_bound_solver.py
│   │   ├── cp_sat_solver.py
│   │   ├── genetic_algorithm_solver.py
│   │   └── simulated_annealing_solver.py
└── README.md
```

- **/data:** Stores raw benchmark datasets (e.g., from TSPLIB, OR-Library).
- **/notebooks:** Contains Jupyter notebooks for exploratory work, analysis, and demonstrations.
- **/src:** Holds the main Python source code.
- **/src/solvers:** Contains the individual wrapper implementations for each algorithm in our portfolio.
- **/src/features:** (Placeholder) Will contain feature extraction logic in Phase 3.

## Environment Setup

This project uses Python with a dedicated Anaconda environment to manage dependencies.

1.  **Create and Activate Anaconda Environment:**
    ```bash
    conda create -n orchestrator python=3.10
    conda activate orchestrator
    ```

2.  **Install Core Libraries:**
    Install the essential libraries for data handling, machine learning, and optimization.
    ```bash
    pip install jupyter pandas scikit-learn matplotlib seaborn
    pip install ortools lightgbm xgboost mealpy simanneal
    ```

## How to Run

The primary entry point for solving problems is the `solve` function located in `src/main.py`. This function acts as a standardized interface for all underlying solvers.

You can see a practical demonstration of how to define problem instances and use the master `solve` function in the `notebooks/01_solver_test.ipynb` notebook. To run it, launch Jupyter:

```bash
jupyter notebook
```

Then, navigate to and open `notebooks/01_solver_test.ipynb`.

```