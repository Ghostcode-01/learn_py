# 🧠 APA ITU SET?
# Set adalah kumpulan data:

# ❌ tanpa duplikat
# ❌ tidak berurutan
# ❌ tidak punya index

# ✅ mutable
# data = {1, 2, 3}

# 📌 PENULISAN SET
# a = {1, 2, 3}
# b = set([1, 2, 2, 3])
# c = set()        # set kosong


# ⚠️
# {}   # ini dictionary, BUKAN set

# ⚙️ ATURAN PENTING SET
# Otomatis hapus duplikat
# Tidak bisa akses pakai index
# Hanya bisa isi immutable data (int, str, tuple)
# List & dict ❌
# {1, [2,3]}  # ERROR

# 🔥 METHOD SET (WAJIB TAU)
# 1️⃣ add(x)

# Tambah 1 item

# s.add(5)

# 2️⃣ update(iterable)

# Tambah banyak item

# s.update([6,7,8])

# 3️⃣ remove(x)

# Hapus item

# s.remove(5)


# ❗ error kalau gak ada

# 4️⃣ discard(x)

# Hapus item (AMAN)

# s.discard(5)

# 5️⃣ pop()

# Hapus item random

# s.pop()

# 6️⃣ clear()

# Kosongkan

# s.clear()

# 🔁 OPERASI MATEMATIKA SET (INI POWER)
# UNION (gabung)
# a | b
# a.union(b)

# INTERSECTION (irisan)
# a & b
# a.intersection(b)

# DIFFERENCE (selisih)
# a - b
# a.difference(b)

# SYMMETRIC DIFFERENCE
# a ^ b
# a.symmetric_difference(b)

# 🔎 CEK RELASI SET
# a.issubset(b)
# a.issuperset(b)
# a.isdisjoint(b)

# 🧪 CONTOH REAL CASE
# 🔹 Hilangkan duplikat
# nilai = [60, 70, 70, 80]
# unik = set(nilai)

# 🔹 Cek keanggotaan (SUPER CEPAT)
# if 70 in unik:
#     print("ada")

# 🔹 Absensi
# hadir = {"andi", "budi"}
# izin = {"budi"}

# bolos = hadir - izin
# DATA AWAL (SIMULASI REAL)
user_web = {"U001", "U002", "U003", "U004"}
user_mobile = {"U003", "U004", "U005", "U006"}
user_transaksi = {"U002", "U003", "U005"}
user_fraud = {"U005", "U009"}
user_blocked = {"U009"}
# Union
all_users = user_web | user_mobile
print(all_users)

# Intersection adalah himpunan baru yang hanya memuat atau berisi elemen-elemen yang ada antara semua himpunan yang dioperasikan 
# contoh kita ingin mencari orang yang aktif melakkukan transaksi tapi kena fraud maka nanti yang tampil hanya user
active_payers = all_users & user_transaksi & user_fraud
print(active_payers)

# DIFFERENCE — User Aman (bukan fraud) adalah himpunan baru yang memuat data yang ada di himpunan pertama tapi tidak ada di himpunan kedua atua himpunan lainnya
# active payers itu h1 user fraud h2
safe_users = active_payers - user_fraud
print(safe_users)

#  SYMMETRIC DIFFERENCE — User Aneh

# user yang muncul di satu sistem tapi tidak di sistem lain atau simple nya himpunan yang menyimpan nilai yang ada di antara dua atau lebih

suspicious_users = user_web ^ user_mobile
print(suspicious_users)

# 🔧 SEMUA METHOD SET KEPPAKE 🔧
# add()
user_fraud.add("U010")

# update()
user_blocked.update({"U005", "U010"})

# remove() vs discard()
user_blocked.remove("U009")   # error kalau gak ada
user_blocked.discard("U999")  # aman, no error

# pop()
random_user = user_blocked.pop()
print("Random blocked:", random_user)


# 📌 dipakai buat sampling

# clear()
user_fraud.clear()


# 📌 reset data harian

# copy()
backup_users = all_users.copy()


# 📌 backup sebelum proses besar

# 🧪 CEK RELASI SET (INDUSTRI BANGET)
# issubset()
print(user_fraud.issubset(user_blocked))


# ➡️ cek apakah semua fraud sudah diblokir

# issuperset()
print(user_blocked.issuperset(user_fraud))

# isdisjoint()
print(user_blocked.isdisjoint(safe_users))


# ➡️ pastikan user aman tidak overlap dengan blocked

# 🏁 FLOW INDUSTRI REAL
if not user_fraud.issubset(user_blocked):
    print("🚨 WARNING: ada user fraud belum diblokir")
else:
    print("✅ Sistem aman")
