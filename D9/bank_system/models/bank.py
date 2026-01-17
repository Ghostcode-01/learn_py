import utils.helpers as helper

class Bank:
    def __init__(self, username_admin, password):
        self._username = username_admin
        self.__password = password

        # Validasi admin
        self.valid = self.load_user()

    def load_user(self):
        # Cek data admin di JSON
        data = helper.load_file()
        for admin in data[1]["admin"]:
            if self._username == admin["username_admin"] and self.__password == admin["password"]:
                return True
        return False

    def show_users(self):
        # Ambil semua user
        data = helper.load_file()
        return data[0]["users"]

    def delete_user(self, username):
        # Hapus user berdasarkan username
        data = helper.load_file()
        data[0]["users"] = [u for u in data[0]["users"] if u["username"] != username]
        helper.save(data)

    def total_balance_bank(self):
        # Total saldo bank
        data = helper.load_file()
        return data[2]["finance"]["saldo"]
