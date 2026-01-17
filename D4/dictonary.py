# # 📦 DICTIONARY (dict) — Python
# # 1️⃣ Apa itu Dictionary?

# # Dictionary = struktur data key–value

# # 🔑 key → 🧾 value
# # Kayak JSON / database mini / object di JS

# user = {
#     "id": 1,
#     "nama": "Budi",
#     "umur": 20,
#     "aktif": True,
# }


# # 📌 Key harus unik, value boleh kembar
# # 📌 Akses pakai key, bukan index
# # 2️⃣ Aturan Penting Dictionary
# # ✅ Key harus immutable
# # string ✅
# # int ✅
# # tuple ✅
# # list ❌
# # dict ❌
# # set ❌

# # ✅ Value bebas:
# # int, string, list, tuple, dict, set, dll

# # 3️⃣ Cara Akses Data
# print(user["nama"])      # Budi


# # ⚠️ Kalau key gak ada → KeyError

# # Aman pakai .get()
# print(user.get("email"))          # None
# print(user.get("email", "N/A"))   # N/A

# # 4️⃣ Tambah & Ubah Data
# user["email"] = "budi@gmail.com"   # tambah
# user["umur"] = 21                 # ubah

# print(user)
# # 📌 Tambah & ubah sintaksnya sama

# # 5️⃣ Hapus Data
# del user["aktif"]

# # pop()
# umur = user.pop("umur")

# # popitem() → hapus terakhir
# user.popitem()

# # clear()
# user.clear()

# # 6️⃣ Looping Dictionary
# # Key saja
# for k in user:
#     print(k)

# # Value saja
# for v in user.values():
#     print(v)

# # Key + Value
# for k, v in user.items():
#     print(k, "=", v)


# # 📌 items() = PALING SERING DIPAKAI di industri

# # 7️⃣ Cek Key / Value
# "nama" in user        # True
# "Budi" in user.values()

# # 8️⃣ Copy Dictionary
# user2 = user.copy()


# # ⚠️ Shallow copy

# # dict di dalam dict → masih nyambung

# # 9️⃣ Update Banyak Data
# user.update({
#     "umur": 22,
#     "status": "premium"
# })

# # 🔥 10️⃣ Dictionary Bersarang (SUPER PENTING)

# # Dipakai di:
# # API
# # JSON
# # Database
# # Backend

# users = {
#     "U001": {
#         "nama": "Andi",
#         "saldo": 50000
#     },
#     "U002": {
#         "nama": "Budi",
#         "saldo": 75000
#     }
# }

# print(users["U001"]["saldo"])

# # 11️⃣ Dictionary + List
# produk = {
#     "nama": "Laptop",
#     "harga": 12000000,
#     "warna": ["hitam", "silver"]
# }

# # 12️⃣ Method Dictionary (WAJIB HAFAL)
# # Method	Fungsi
# # get()	ambil aman
# # keys()	semua key
# # values()	semua value
# # items()	key + value
# # pop()	hapus by key
# # popitem()	hapus terakhir
# # update()	update banyak
# # clear()	kosongkan
# # copy()	duplikat
# # 13️⃣ Dictionary Comprehension 🔥
# nilai = {"andi": 80, "budi": 60}
# lulus = {k: v for k, v in nilai.items() if v >= 75}

# # 14️⃣ Real Use Case INDUSTRI
# # Login System
# users = {
#     "admin": "12345",
#     "user": "abcde"
# }

# if users.get("admin") == "12345":
#     print("Login sukses")


# 15️⃣ Perbandingan Cepat
# Struktur	Akses	Duplikat
# list	index	boleh
# tuple	index	boleh
# set	-	tidak
# dict	key	key unik
# 🧠 Kalimat Sakti

# Kalau datanya punya "nama" → pakai dict,
# kalau cuma urutan → list

# 📦 DATA AWAL ABSENSI
# key  = (tanggal, shift, kode_karyawan)
# value = status kehadiran (hadir / izin / alpha)
absensi = {
    ("2026-01-01", "pagi", "K001"): "hadir",
    ("2026-01-01", "malam", "K002"): "izin",
    ("2026-01-02", "pagi", "K001"): "alpha",
}

# tampilkan menu utama
print("\n 1. AKSES DATA 2. TAMBAH/UBAH DATA 3. TAMPILKAN SEMUA ABSENSI 4. EXIT")

# penanda apakah program masih berjalan atau berhenti
start = True

# loop utama program
while start:

    # user memilih menu (1 / 2 / 3 / 4)
    option = int(input("masukkan angka di atas: "))

    # ================= MENU 1 : AKSES DATA =================
    if option == 1:
        # user memasukkan identitas absensi yang ingin dicek
        tanggal = input("masukkan tanggal (YYYY-MM-DD): ")
        shift = input("masukkan shift: ")
        kode_karyawan = input("masukkan kode karyawan: ")

        # cek apakah data ada di dictionary
        if (tanggal, shift, kode_karyawan) not in absensi:
            print("❌ data tidak ditemukan")
        else:
            # ambil value berdasarkan key
            key = (tanggal, shift, kode_karyawan)
            print("✅ status kehadiran:", absensi.get(key))

    # ================= MENU 2 : ADMIN =================
    elif option == 2:
        # validasi password admin
        password = ""
        while password != "ghost":
            password = input("masukkan password admin: ")

        print("✅ welcome admin")

        # pilih aksi admin
        command = int(input("1. tambah/ubah  2. hapus : "))

        # -------- TAMBAH / UBAH DATA --------
        if command == 1:
            # pastikan semua input tidak kosong
            while not all([
                tanggal := input("tanggal (YYYY-MM-DD): "),
                shift := input("shift: "),
                kode_karyawan := input("kode karyawan: "),
                value := input("status kehadiran: ")
            ]):
                print("❌ input tidak boleh kosong")

            # tambah atau update data absensi
            absensi[(tanggal, shift, kode_karyawan)] = value
            print("✅ data berhasil disimpan")

        # -------- HAPUS DATA --------
        if command == 2:
            # input key yang ingin dihapus
            while not all([
                tanggal := input("tanggal (YYYY-MM-DD): "),
                shift := input("shift: "),
                kode_karyawan := input("kode karyawan: "),
            ]):
                print("❌ input tidak boleh kosong")

            # hapus data dari dictionary
            del absensi[(tanggal, shift, kode_karyawan)]
            print("🗑️ data berhasil dihapus")

    # ================= MENU 3 : TAMPILKAN SEMUA DATA =================
    elif option == 3:
        # loop seluruh isi dictionary absensi
        for (tanggal, shift, kode_karyawan), value in absensi.items():
            print(tanggal, "|", shift, "|", kode_karyawan, "|", value)

    # ================= MENU 4 : EXIT =================
    elif option == 4:
        # hentikan program
        start = False

# 📝 TUGAS WAJIB (KERJAIN SEMUA)
# 🔑 BAGIAN A — AKSES DATA

# 1️⃣ Ambil status absensi K001 tanggal 2026-01-01 shift pagi
# 2️⃣ Ambil status absensi K002 tanggal 2026-01-01 shift malam

# ➕ BAGIAN B — TAMBAH & UBAH DATA

# 3️⃣ Tambahkan absensi:

# tanggal: 2026-01-02
# shift: malam
# karyawan: K003

# status: hadir

# 4️⃣ Ubah status K001 tanggal 2026-01-02 shift pagi jadi hadir

# ❌ BAGIAN C — HAPUS DATA

# 5️⃣ Hapus absensi K002 tanggal 2026-01-01 shift malam

# 🔍 BAGIAN D — LOGIKA

# 6️⃣ Cek apakah absensi
# ("2026-01-03", "pagi", "K001")
# ada atau tidak (tanpa error)

# 🔄 BAGIAN E — LOOPING

# 7️⃣ Loop semua data absensi dan tampilkan:

# Tanggal | Shift | ID | Status

# 🧠 BAGIAN F — ANALISIS (PAKE KATA-KATA)

# 8️⃣ Kenapa tuple cocok jadi key di kasus ini?
# 9️⃣ Kalau key diganti list, apa yang terjadi?
# 🔟 Kenapa dict lebih cocok daripada list of list?

# ⛔ ATURAN KERAS

# ❌ Jangan ubah struktur data

# ❌ Jangan pake list sebagai key

# ❌ Jangan pake database

# ✅ Fokus dict + tuple