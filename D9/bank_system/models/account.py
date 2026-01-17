import utils.helpers as helper

class Account:
    def __init__(self, username, password):
        # Data dasar user
        self._username = username
        self.__password = password
        self.__balance = 0

        # Validasi login user
        self.is_valid = self.load_user()

    def load_user(self):
        # Ambil data dari JSON
        data = helper.load_file()

        # Cek username & password
        for user in data[0]['users']:
            if user["username"] == self._username and user["password"] == self.__password:
                info = user['info']
                self.__balance = info["saldo"]
                self.__premium = info["premium"]
                return True
        return False

    def __save_user(self):
        # Simpan perubahan saldo user ke JSON
        data = helper.load_file()
        for user in data[0]["users"]:
            if user["username"] == self._username:
                user["password"] = self.__password
                user["info"]["saldo"] = self.__balance
                user["info"]["premium"] = self.__premium
        helper.save(data)

    def deposit(self, amount):
        # Validasi minimal deposit
        if amount <= 100000:
            print("Deposit minimal 100.000")
            return False

        # Hitung bunga
        pendapatan = helper.pendapatan_bunga(amount)
        saldo_added = helper.potong_bunga(amount)

        # Tambah saldo user
        self.__balance += saldo_added

        # Update data bank
        data = helper.load_file()
        data[2]['finance']['saldo'] += pendapatan
        helper.save(data)

        return True

    def withdraw(self, amount):
        # Validasi withdraw
        if amount <= 0:
            print("Jumlah tidak valid")
            return False

        # Limit withdraw untuk non-premium
        if amount >= 100_000_000 and self.__premium != "true":
            print("Harus premium")
            return False

        if amount > self.__balance:
            print("Saldo tidak cukup")
            return False

        # Kurangi saldo
        self.__balance -= amount
        self.__save_user()
        return True

    def check_saldo(self):
        # Kembalikan saldo user
        return self.__balance
