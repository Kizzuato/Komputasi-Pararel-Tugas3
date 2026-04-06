import multiprocessing
import time
import os

# NRP: 152024127 
# Nama: Dzakiyya Puteri Aulia

# Tugas 1: Fungsi untuk menghitung faktorial
def hitung_faktorial(n):
    print(f"[TASK 1] Sedang menghitung faktorial dari {n}...")
    print(f"ID Proses Task 1: {os.getpid()}")
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
        time.sleep(0.5) # Kasih jeda dikit biar kelihatan prosesnya
    print(f"-> Hasil Faktorial {n} = {hasil}")

# Tugas 2: Fungsi untuk mengecek bilangan prima atau bukan
def cek_bilangan_prima(n):
    print(f"[TASK 2] Sedang mengecek apakah {n} itu prima...")
    print(f"ID Proses Task 2: {os.getpid()}")
    prima = True
    if n < 2:
        prima = False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                prima = False
                break
            time.sleep(0.5)
    
    if prima:
        print(f"-> {n} adalah Bilangan Prima!")
    else:
        print(f"-> {n} bukan Bilangan Prima.")

# Tugas 3: Fungsi untuk menjumlahkan isi sebuah list
def jumlahin_list(daftar_angka):
    print(f"[TASK 3] Sedang menjumlahkan isi list: {daftar_angka}...")
    print(f"ID Proses Task 3: {os.getpid()}")
    total = 0
    for x in daftar_angka:
        total += x
        time.sleep(0.5)
    print(f"-> Hasil Penjumlahan List = {total}")

if __name__ == "__main__":
    print("-" * 50)
    print("PROGRAM TASK PARALLELISM")
    print("NRP: 152024127 (Ganjil)")
    print("Nama: Dzakiyya Puteri Aulia")
    print("-" * 50)

    # Menyiapkan data input
    angka_faktorial = 6
    angka_cek = 13
    kumpulan_angka = [10, 20, 30, 40]

    # Membuat proses yang berbeda untuk setiap tugas (Task Parallelism)
    # Di sini tugasnya berbeda-beda (beda fungsi)
    proses1 = multiprocessing.Process(target=hitung_faktorial, args=(angka_faktorial,))
    proses2 = multiprocessing.Process(target=cek_bilangan_prima, args=(angka_cek,))
    proses3 = multiprocessing.Process(target=jumlahin_list, args=(kumpulan_angka,))

    # Menjalankan semua tugas secara bersamaan
    proses1.start()
    proses2.start()
    proses3.start()

    # Nunggu semuanya sampe beres
    proses1.join()
    proses2.join()
    proses3.join()

    print("-" * 50)
    print("Semua tugas sudah selesai dijalankan.")
