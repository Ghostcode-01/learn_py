# 🧠 ERROR HANDLING — CHEAT SHEET
# 📌 Konsep Inti

# Error ≠ program mati

# Error = kondisi yang harus ditangani

# Target: program tetap jalan & aman

# 🧱 STRUKTUR DASAR
# try:
#     kode_berisiko
# except ErrorType:
#     penanganan

# 🧨 EXCEPTION PALING PENTING (WAJIB HAFAL)
# Exception	Terjadi Saat
# ValueError	nilai salah (int("a"))
# TypeError	tipe salah (10 + "5")
# ZeroDivisionError	bagi nol
# IndexError	index list out
# KeyError	key dict gak ada
# FileNotFoundError	file gak ada
# PermissionError	gak punya izin
# ImportError	gagal import
# AttributeError	method gak ada
# NameError	variabel belum ada
# JSONDecodeError	JSON rusak
# Exception	payung semua error
# ✅ POLA BENAR (INDUSTRI)
try:
    x = int(input())
    y = 10 / x
except ValueError:
    print("Input harus angka")
except ZeroDivisionError:
    print("Tidak boleh nol")
except Exception as e:
    print("Error lain:", e)


# 📌 urutan: spesifik → umum

# ❌ YANG DILARANG
# except:
#     pass


# 💀 error ketelen
# 💀 debugging neraka

# 🧠 else & finally
# try:
#     ...
# except Error:
#     ...
# else:
#     # jalan kalau sukses
# finally:
#     # SELALU jalan

# 📂 FILE HANDLING AMAN
# try:
#     with open("data.json") as f:
#         data = json.load(f)
# except FileNotFoundError:
#     data = []
# except json.JSONDecodeError:
#     data = []

# 🚨 RAISE ERROR (VALIDASI)
# if nilai < 0:
#     raise ValueError("Nilai tidak boleh negatif")

# 🧬 CUSTOM ERROR (ADVANCED)
# class DataKosongError(Exception):
#     pass

# 🧠 DEBUG ERROR CEPAT
# except Exception as e:
#     print(type(e))
#     print(e)

# 🎯 POLA PROJECT YANG BENAR

# Function return data

# UI (print) di main

# Error ditangani, bukan diabaikan

# 🧪 TEMPLATE PROJECT (SIAP PAKAI)
# def load_data():
#     try:
#         with open("data.json") as f:
#             return json.load(f)
#     except:
#         return []