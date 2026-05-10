import multiprocessing
import time
import random

def worker_task(task_id):
    """
    Simulates a computational task that takes a variable amount of time.
    By using dynamic distribution, faster workers will pick up more tasks,
    optimizing the overall execution time.
    """
    # Simulate uneven workload
    sleep_time = random.uniform(0.1, 0.5)
    print(f"Worker processing Task {task_id} (Expected time: {sleep_time:.2f}s)")
    time.sleep(sleep_time)
    return task_id, sleep_time

def dynamic_distribution():
    num_tasks = 20
    tasks = list(range(num_tasks))
    num_workers = 4
    
    print(f"NRP: 152024127 (Uneven -> Using Dynamic Distribution)")
    print(f"Distributing {num_tasks} tasks dynamically among {num_workers} workers...")
    print("-" * 50)
    
    start_time = time.time()
    
    # Using multiprocessing.Pool for dynamic load balancing.
    # imap_unordered dynamically assigns tasks to workers as soon as they become idle.
    with multiprocessing.Pool(processes=num_workers) as pool:
        results = pool.imap_unordered(worker_task, tasks)
        
        total_work_time = 0
        for task_id, duration in results:
            total_work_time += duration

    end_time = time.time()
    actual_time = end_time - start_time
    
    # Theoretical optimal time is total work divided by number of workers
    expected_optimal = total_work_time / num_workers
    
    print("-" * 50)
    print("Execution Summary:")
    print(f"Total pure work time (if sequential): {total_work_time:.4f} seconds")
    print(f"Expected optimal time (perfect distribution): {expected_optimal:.4f} seconds")
    print(f"Actual execution time (Dynamic Distribution): {actual_time:.4f} seconds")
    
    # Show that the code reached near optimal time
    efficiency = (expected_optimal / actual_time) * 100
    print(f"Efficiency: {efficiency:.2f}% (Shows when the code expects optimal time)")

if __name__ == '__main__':
    dynamic_distribution()
