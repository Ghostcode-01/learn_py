# 1️⃣ BUKA FILE (AKAR SEGALANYA)
# Mode file:
# Mode	Fungsi
# "r"	baca
# "w"	tulis (hapus lama)
# "a"	tambah
# "x"	buat baru
# ❌ Cara lama (jangan biasain)
# file = open("../error_handling.py", "r")
# print(file.read())
# file.close()

# ✅ Cara BENAR (with)
with open("./learn_python/day6/file.txt", "w") as file:
    file.write('bajinganlah susah kali')
    print(file.read())


# # 📌 Auto close → aman.
# # 2️⃣ TULIS FILE
# with open("data.txt", "w") as file:
#     file.write("Halo Python\n")


# # ⚠️ "w" = overwrite.

# # 3️⃣ TAMBAH DATA
# with open("data.txt", "a") as file:
#     file.write("Data baru\n")

# # 4️⃣ BACA PER BARIS
# with open("data.txt", "r") as file:
#     for line in file:
#         print(line.strip())

# # 5️⃣ FILE CSV (DASAR)
# import csv

# with open("data.csv", newline="") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)