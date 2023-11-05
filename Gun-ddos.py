import requests
import threading
import time
import os

# Fungsi untuk membuat permintaan ke URL dan mengukur waktunya
def make_request(url):
    start_time = time.time()
    try:
        response = requests.get(url)
        response.raise_for_status()
        end_time = time.time()
        elapsed_time = end_time - start_time
        if response.status_code == 200:
            print(f"Permintaan ke {url} berhasil dalam {elapsed_time:.2f} detik")
        else:
            print(f"Permintaan ke {url} gagal dengan kode status {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Terjadi kesalahan saat melakukan permintaan ke {url}: {str(e)}")

# Fungsi utama untuk mengirim permintaan dengan threading
def send_requests(num_requests, url):
    threads = []

    for _ in range(num_requests):
        t = threading.Thread(target=make_request, args=(url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    print("Penulis: Nama Penulis Anda")  # Ganti "Nama Penulis Anda" dengan nama Anda
    
    while True:
        url = input("Masukkan URL target: ")
        num_requests = int(input("Masukkan jumlah permintaan: "))

        try:
            send_requests(num_requests, url)
        except KeyboardInterrupt:
            print("\nEksekusi program dihentikan dengan Ctrl + C.")

        repeat = input("Ingin mengulangi permintaan (y/n)? ").lower()
        if repeat != 'y':
            break
