# # DAY 9 — FUNCTION (AKAR LOGIKA PROGRAM)
# # 🧠 APA ITU FUNCTION?

# # Function = blok kode yang bisa dipakai ulang
# # Tujuan:
# # anti ngulang kode
# # lebih rapi
# # lebih gampang di-debug
# # siap scale (AI, backend, data)

# # 1️⃣ SINTAKS DASAR
# def sapa():
#     print("Halo Python")


# # Panggil:
# sapa()


# # 📌 def → define function
# # 📌 Nama function → kata kerja (best practice)

# # 2️⃣ FUNCTION + PARAMETER
# def sapa(nama):
#     print(f"Halo {nama}")

# sapa("Samuel")

# # 3️⃣ MULTIPLE PARAMETER
# def tambah(a, b):
#     print(a + b)

# # 4️⃣ RETURN (INI KRUSIAL)
# def tambah(a, b):
#     return a + b

# hasil = tambah(5, 3)
# print(hasil)


# # 📌 return:
# # mengembalikan nilai
# # menghentikan function
# # 5️⃣ FUNCTION TANPA & DENGAN RETURN
# # ❌ Salah:

# x = print("halo")


# # ✅ Benar:
# def halo():
#     return "halo"

# # 6️⃣ DEFAULT PARAMETER
# def sapa(nama="User"):
#     print(f"Halo {nama}")

# # 7️⃣ SCOPE (AKAR BUG PALING SERING)
# x = 10  # global

# def test():
#     x = 5  # local
#     print(x)

# test()
# print(x)

# # 📌 Local ≠ Global
# # 8️⃣ *args & **kwargs (ADVANCED DASAR)
# def total(*angka):
#     return sum(angka)

# def user(**data):
#     print(data["nama"])

# TUGASSS
# function hitung luas persegi
def hitung_luas_persegi_panjang (panjang, lebar):
    luas = panjang * lebar
    print('luas nya adalah ', luas)

hitung_luas_persegi_panjang(20, 40)
# function cek ganjil genap
def cek_ganjil_genap(*angka):
    for a in angka:
        if a!=0 and int(a) % 2==0:
            print(a, '=', 'genap')
        else:
            print(a, '=', 'ganjil')

cek_ganjil_genap(1,2,3,4,5,6,7,8,9,10)
# function konversi suhu
def convert(nilai, suhu1, suhu2):
    suhu1 = suhu1.lower()
    suhu2 = suhu2.lower()

    if suhu1 == suhu2:
        return nilai

    # Celsius ke ...
    if suhu1 == 'c' and suhu2 == 'f':
        return (9 / 5 * nilai) + 32
    elif suhu1 == 'c' and suhu2 == 'k':
        return nilai + 273.15

    # Fahrenheit ke ...
    elif suhu1 == 'f' and suhu2 == 'c':
        return (nilai - 32) * 5 / 9
    elif suhu1 == 'f' and suhu2 == 'k':
        return (nilai - 32) * 5 / 9 + 273.15

    # Kelvin ke ...
    elif suhu1 == 'k' and suhu2 == 'c':
        return nilai - 273.15
    elif suhu1 == 'k' and suhu2 == 'f':
        return (nilai - 273.15) * 9 / 5 + 32

    else:
        return "❌ konversi tidak valid"

print(convert(100, 'c', 'f'))  # 212
print(convert(0, 'c', 'k'))    # 273.15
print(convert(32, 'f', 'c'))   # 0
print(convert(300, 'k', 'c'))  # 26.85

# function hitung diskon
def discount(harga):
    if harga >= 200000:
        diskon = 0.2
        print('total setelah diskon:', harga - harga * diskon)
    elif harga >= 100000:
        diskon = 0.1
        print('total setelah diskon:', harga - harga * diskon)
    else:
        print('anda gak dapat diskon, harga:', harga)

discount(100000)