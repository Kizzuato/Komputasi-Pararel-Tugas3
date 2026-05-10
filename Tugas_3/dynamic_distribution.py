import multiprocessing
import time
import random

# untuk mensimulasikan task komputasi dengan waktu eksekusi yang bervariasi
def worker_task(task_id):
    # untuk mensimulasikan beban kerja yang tidak merata (uneven workload)
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
    
    # untuk membuat pool worker dan mendistribusikan task secara dinamis
    # imap_unordered akan memberikan task baru ke worker yang sudah selesai (idle)
    with multiprocessing.Pool(processes=num_workers) as pool:
        results = pool.imap_unordered(worker_task, tasks)
        
        total_work_time = 0
        for task_id, duration in results:
            total_work_time += duration

    end_time = time.time()
    actual_time = end_time - start_time
    
    # untuk menghitung waktu optimal (total kerja dibagi jumlah worker)
    expected_optimal = total_work_time / num_workers
    
    print("-" * 50)
    print("Execution Summary:")
    print(f"Total pure work time (if sequential): {total_work_time:.4f} seconds")
    print(f"Expected optimal time (perfect distribution): {expected_optimal:.4f} seconds")
    print(f"Actual execution time (Dynamic Distribution): {actual_time:.4f} seconds")
    
    # untuk menunjukkan bahwa kode mencapai waktu mendekati optimal
    efficiency = (expected_optimal / actual_time) * 100
    print(f"Efficiency: {efficiency:.2f}% (Shows when the code expects optimal time)")

if __name__ == '__main__':
    dynamic_distribution()
