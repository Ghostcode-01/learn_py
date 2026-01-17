print("SISTEM MANAJEMEN DATA SISWA ANTI CRASH")

# import semua function dari utils.py
import utils

# loop utama program
while True:
    print("\n1. Tambah siswa")
    print("2. Lihat data")
    print("3. Keluar")

    # input pilihan menu
    pilih = input("Pilih: ")

    # jika pilih tambah siswa
    if pilih == "1":
        utils.add_student()

    # jika pilih lihat data
    elif pilih == "2":
        utils.show_data()

    # jika keluar program
    elif pilih == "3":
        utils.log("Program selesai")
        break

    # jika input tidak valid
    else:
        print("Pilihan salah")
