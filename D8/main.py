# import konfigurasi aplikasi
import config_utils

# import function hitung progress dari stats_utils
from stats_utils import hitung_progress

# import semua fungsi terkait task
import task_utils


# fungsi utama program
def main():
    # load konfigurasi aplikasi (nama app, versi, mode debug)
    config_utils.load_config(
        app_name="Task Manager CLI",
        version="1.0",
        debug=True
    )

    # tampilkan menu fitur
    print('(1)tambah task, (2)lihat semua task, (3)hitung progress, (4)hapus_task, (5)close')

    # loop utama agar program terus berjalan
    while True:
        try:
            # input pilihan menu
            pilih = int(input('masukkan angka diatas untuk menjalankan program: '))
        except:
            # jika input bukan angka
            print('masukkan angka')
            continue

        # tambah task baru
        if pilih == 1:
            task_utils.tambah_task()

        # tampilkan semua task
        elif pilih == 2:
            task_utils.tampilkan_task()

        # hitung progress task
        elif pilih == 3:
            progress = hitung_progress()
            print(f"Progress tugas: {progress}%")

        # hapus task berdasarkan indeks
        elif pilih == 4:
            task_utils.hapus_task()

        # keluar dari program
        elif pilih == 5:
            break


# jalankan main() hanya jika file ini dijalankan langsung
if __name__ == "__main__":
    main()
