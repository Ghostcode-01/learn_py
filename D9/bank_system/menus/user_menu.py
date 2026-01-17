def users(account):
    # Menu user (deposit, withdraw, cek saldo)
    while True:
        try:
            print("\n1. Deposit\n2. Withdraw\n3. Cek Saldo\n4. Logout")
            i = int(input(">> "))
        except ValueError:
            print("Input harus angka")
            continue

        if i == 1:
            # Deposit saldo
            amt = int(input("Jumlah: "))
            print("OK" if account.deposit(amt) else "Gagal")

        elif i == 2:
            # Tarik saldo
            amt = int(input("Jumlah: "))
            print("OK" if account.withdraw(amt) else "Gagal")

        elif i == 3:
            # Cek saldo saat ini
            print("Saldo:", account.check_saldo())

        elif i == 4:
            # Logout user
            break
