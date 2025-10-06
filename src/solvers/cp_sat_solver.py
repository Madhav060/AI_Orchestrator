import collections
from ortools.sat.python import cp_model

def solve_jssp_with_cp_sat(problem_instance):
    """
    Solves a Job-Shop Scheduling Problem instance using the CP-SAT solver.
    """
    jobs_data = problem_instance["jobs"]
    # --- THIS IS THE CORRECTED LINE ---
    machines_count = 1 + max(task[0] for job in jobs_data for task in job)
    
    all_machines = range(machines_count)
    # Compute horizon dynamically as the sum of all durations.
    horizon = sum(task[1] for job in jobs_data for task in job)

    # Create the CP-SAT model.
    model = cp_model.CpModel()

    # Create named tuple to store task data.
    task_type = collections.namedtuple('task_type', 'start end interval')
    
    # Create a dictionary to hold all tasks.
    all_tasks = {}
    # Create a dictionary to map each machine to its intervals.
    machine_to_intervals = collections.defaultdict(list)

    # Create all interval variables.
    for job_id, job in enumerate(jobs_data):
        for task_id, task in enumerate(job):
            machine, duration = task
            suffix = f'_{job_id}_{task_id}'
            start_var = model.NewIntVar(0, horizon, 'start' + suffix)
            end_var = model.NewIntVar(0, horizon, 'end' + suffix)
            interval_var = model.NewIntervalVar(start_var, duration, end_var, 'interval' + suffix)
            all_tasks[job_id, task_id] = task_type(start=start_var, end=end_var, interval=interval_var)
            machine_to_intervals[machine].append(interval_var)

    # Add "no overlap" constraints for each machine.
    for machine in all_machines:
        model.AddNoOverlap(machine_to_intervals[machine])

    # Add precedence constraints for tasks within each job.
    for job_id, job in enumerate(jobs_data):
        for task_id in range(len(job) - 1):
            model.Add(all_tasks[job_id, task_id + 1].start >= all_tasks[job_id, task_id].end)

    # Define the objective: minimize the makespan (the end time of the last task).
    obj_var = model.NewIntVar(0, horizon, 'makespan')
    model.AddMaxEquality(obj_var, [all_tasks[job_id, len(job) - 1].end for job_id, job in enumerate(jobs_data)])
    model.Minimize(obj_var)

    # Create a solver and solve the model.
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    # Extract and return the solution.
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        solution = collections.defaultdict(list)
        for job_id, job in enumerate(jobs_data):
            for task_id, task in enumerate(job):
                machine, duration = task
                start_time = solver.Value(all_tasks[job_id, task_id].start)
                solution[machine].append({
                    "job": job_id,
                    "task": task_id,
                    "start": start_time,
                    "end": start_time + duration
                })
        return solution, solver.ObjectiveValue()
    else:
        # Return an empty solution if no solution is found.
        return None, float('inf')