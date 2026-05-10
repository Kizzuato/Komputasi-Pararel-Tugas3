# Komputasi Paralel - Tugas 3: Dynamic Distribution

**NRP:** 152024127 (Ganjil / Uneven)  
**Materi:** Dynamic Distribution untuk Load Balancing (Menunjukkan saat kode mencapai waktu optimal yang diharapkan).

## 1. Source Code (`dynamic_distribution.py`)
Kode ini menggunakan `multiprocessing.Pool` dengan `imap_unordered` di Python. Karena waktu yang dibutuhkan tiap task berbeda-beda (uneven), pekerja (worker) yang selesai lebih cepat akan mengambil task baru dari antrian secara dinamis. Ini adalah contoh dari **Dynamic Load Balancing/Distribution**.

```python
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
```

## 2. Capture (Compile & Execute Output)

```text
NRP: 152024127 (Uneven -> Using Dynamic Distribution)
Distributing 20 tasks dynamically among 4 workers...
--------------------------------------------------
Worker processing Task 0 (Expected time: 0.27s)
Worker processing Task 1 (Expected time: 0.25s)
Worker processing Task 2 (Expected time: 0.24s)
Worker processing Task 3 (Expected time: 0.31s)
Worker processing Task 4 (Expected time: 0.24s)
Worker processing Task 5 (Expected time: 0.16s)
Worker processing Task 6 (Expected time: 0.45s)
Worker processing Task 7 (Expected time: 0.24s)
Worker processing Task 8 (Expected time: 0.32s)
Worker processing Task 9 (Expected time: 0.21s)
Worker processing Task 10 (Expected time: 0.30s)
Worker processing Task 11 (Expected time: 0.36s)
Worker processing Task 12 (Expected time: 0.47s)
Worker processing Task 13 (Expected time: 0.24s)
Worker processing Task 14 (Expected time: 0.21s)
Worker processing Task 15 (Expected time: 0.43s)
Worker processing Task 16 (Expected time: 0.38s)
Worker processing Task 17 (Expected time: 0.26s)
Worker processing Task 18 (Expected time: 0.11s)
Worker processing Task 19 (Expected time: 0.40s)
--------------------------------------------------
Execution Summary:
Total pure work time (if sequential): 5.8315 seconds
Expected optimal time (perfect distribution): 1.4579 seconds
Actual execution time (Dynamic Distribution): 1.7312 seconds
Efficiency: 84.21% (Shows when the code expects optimal time)
```

## 3. Penjelasan Eksekusi Task (Brief Explanation)

- **Worker pool creation (`multiprocessing.Pool`)**: Membuat 4 proses pekerja independen.
- **Uneven Workload Simulation**: Tiap task diberikan beban eksekusi acak antara `0.1s` hingga `0.5s` (mewakili workload dinamis tak tertebak di dunia nyata).
- **Dynamic Assignment (`imap_unordered`)**: Metode ini tidak mendistribusikan task secara kaku dari awal. Jika *worker* A kebetulan menangani task yang ringan (misal `0.11s`) ia akan langsung menganggur (idle) dan langsung meminta task baru berikutnya dari sistem pool.  
- **Expected Optimal Time**: Dihitung dari menjumlahkan semua *pure work time* secara sekuesial lalu membaginya dengan jumlah `worker`. Pada program ditunjukkan perbandingan **Actual execution time** dengan **Expected optimal time**, membuktikan bahwa distribusi dinamis mencapai efisiensi yang sangat tinggi (**~84-90%**) pada beban kerja heterogen.
