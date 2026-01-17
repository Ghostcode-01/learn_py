class Account:
    def __init__ (self, account_number, owner_name):
        self.__account_number = account_number
        self.__owner_name = owner_name
        self.__balance = 0
    

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            print('deposit harus lebih dari 0')
            return
        if amount < 100000:
            print('deposit minimal 100 ribu')
            return
        self.__balance += amount

    def withdraw(self, amount):
        if amount < 0:
            print('deposit tidak boleh minus')
        if amount > self.__balance or 100000 > self.__balance - amount:
            print('saldo yang tersisa harus 100000')
        else:
            self.__balance-=amount
    def account_info(self):
        print("=== INFO AKUN ===")
        # akses attribute PRIVATE dari DALAM class (boleh)
        print(f"No Rekening : {self.__account_number}")
        print(f"Pemilik     : {self.__owner_name}")
        print(f"Saldo       : {self.__balance}")

class premium_account(Account):
    def __init__(self, account_number, owner_name):
        super().__init__(account_number, owner_name)
        self.__withdraw_limit= 1_000_000
        self.__deposit_bonus = 0.05

    def withdraw(self, amount):
        if amount <= 0:
            print("Error: jumlah penarikan harus lebih dari 0")
            return
        if amount > self.__withdraw_limit:
            print("Error: melebihi limit tarik premium")
            return
        
        # saldo diambil lewat METHOD parent (ENCAPSULATION)
        if amount > self.get_balance()- amount< 100000:
            print("Error: saldo minimal premium 100000")
            return

        # PAKAI parent method secara aman
        self._Account__balance -= amount
    def deposit(self, amount):
        if amount <= 0:
            print("Error: jumlah deposit harus lebih dari 0")
            return
        bonus = amount * self.__deposit_bonus
        total = amount + bonus

        print(f"Deposit premium: {amount} + bonus {bonus}")
        
        # pakai deposit parent
        super().deposit(total)

class user:
    def __init__(self, id_user, nama):
        self.id_user = id_user
        self.nama = nama
    def login(self):
        print(f'{self.nama} berhasil login')
    def logout (self):
        print(f'{self.nama} berhasil logout')

class Admin(user):
    def __init__(self, id_user,nama ):
        super().__init__(id_user, nama)
        self.role = 'admin'
    
    def tambah_siswa(self, siswa):
        print(f'admin menambahkan siswa bernama: {siswa}')
    
    def tambah_guru(self, guru):
        print(f'admin menambahkan guru bernama: {guru}')
    
    def lihat_semua_user(self, users):
        for user in users:
            print(user.nama)

class guru(user):
    def __init__(self, id_user, nama, mapel):
        super().__init__(id_user, nama)
        self.mapel = mapel
        self.role = "Guru"
    def input_nilai(self,siswa, nilai):
        siswa.nilai = nilai
        print(f'nilai {siswa.nama} = {nilai}')
    def lihat_siswa (self, daftar_nilai):
        for siswa in daftar_nilai:
            print(siswa.nama)
            
class siswa(user):
    def __init__(self, id_user, nama):
        super().__init__(id_user, nama)
        self.role = 'siswa'
        self.nilai = None
    def lihat_nilai(self ):
        print(f'nilai kamu {self.nilai}')
    def update_nama(self, nama_baru):
        self.nama = nama_baru
        print('nama berhasil di update')


admin = Admin(1, "Samuel")

akun = Account("123456", "Samuel")

akun.deposit(200000)
akun.withdraw(50000)
akun.account_info()

akun_premium = premium_account("999999", "Samuel Premium")

akun_premium.deposit(200000)
akun_premium.withdraw(100000)
akun_premium.account_info()

admin = Admin(1, "Samuel")
guru1 = guru(2, "Pak Budi", "MTK")
siswa1 = siswa(3, "Andi")
siswa2 = siswa(4, "Budi")

admin.login()
guru1.login()
siswa1.login()

guru1.input_nilai(siswa1, 90)
guru1.input_nilai(siswa2, 85)

siswa1.lihat_nilai()
siswa2.lihat_nilai()

users = [admin, guru1, siswa1, siswa2]
admin.lihat_semua_user(users)
