import utils.helpers as utilities

def admin_menu(admin):
    # Loop menu admin
    while True:
        print("\n1. Lihat User\n2. Hapus User\n3. Total Saldo Bank\n0. Logout")
        pilih = input(">> ")

        if pilih == "1":
            # Tampilkan semua username user
            for u in admin.show_users():
                print(u["username"])

        elif pilih == "2":
            # Hapus user berdasarkan username
            uname = input("Username >> ")
            admin.delete_user(uname)

        elif pilih == "3":
            # Lihat total saldo bank
            print("Finance:", admin.total_balance_bank())

        elif pilih == "0":
            # Keluar dari menu admin
            break
