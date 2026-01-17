import json
import random
from models.account import Account
from models.bank import Bank
import menus.user_menu as menu_user
import menus.admin_menu as menu_admin

def login_user():
    while True:
        role = input("Login sebagai (admin/user) >> ").lower()
        if role in ("admin", "user"):
            break
        print("masukkan admin atau user")
        
    if role == "admin":
        username = input("username >> ")
        while True:
            try:
                password =int(input("password >> "))
                break
            except ValueError:
                print("masukkan angka")
        B = Bank(username, password)
        if not B.valid:
            print("❌ Username atau password salah")
            return
        menu_admin.admin_menu(B)
    else: 
        username = input("username >> ")
        while True:
            try :
                password = int(input("Password >> "))
                break
            except ValueError:
                print("masukkan angka")
        acc = Account(username, password)
        if not acc.is_valid:
            print("❌ Username atau password salah")
            return
        menu_user.users(acc)
    

def register_user():
    nama = input("masukkan username>> ")
    try:
        password = int(input("masukkan password>> "))
    except ValueError:
        print("masukkan angka")
    nama_lengkap = input("masukkan nama_lengkap>> ")

    no_rek = random.randint(100000000, 999999999)
    default_premium = "false"
    try:
        deposit = int(input("masukkan angka min 100.000"))
    except ValueError:
        print('masukkan angka!!')
    data = load_file()
    data_user = {
        "username": nama,
        "password": password,
        "info": {
            "no_rek" : no_rek,
            "nama_pemilik": nama_lengkap,
            "premium": default_premium,
            "saldo" :deposit
        }
    }
    data[0]["users"].append(data_user)
    save(data)


def pendapatan_bunga(amount):
    bunga = 2/100
    pendapatan_bunga = amount * bunga
    return pendapatan_bunga

def potong_bunga(amount):
    bunga = 2/100
    saldo_added = amount-(amount * bunga)
    return saldo_added
def load_file():
    try:
        with open('./L_P/D9/data/central_da.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # jika file belum ada
        print('data gak ada')
        return []
def save(data):
    try:
        with open('./L_P/D9/data/central_da.json', 'w') as f:
            json.dump(data, f, indent=4)
            print("berhasil disimpan")
    except FileNotFoundError:
        # jika file belum ada
        print('data gak ada')
        return []