import utils.helpers as helper

def main():
    print("WELCOME TO GHOST BANK")

    # Menu utama aplikasi
    while True:
        print("1. Login\n2. Register\n3. Exit")
        try:
            i = int(input(">> "))
        except ValueError:
            print("Input harus angka")
            continue

        if i == 1:
            helper.login_user()
        elif i == 2:
            helper.register_user()
        elif i == 3:
            break

main()
