# # list = wadah data berurutan, yang bisa diubah, bisa duplikat, bisa bersarang dan bisa bercampur tipe

# data = [1, 2, 3]
# nama = ["andi", "budi", "caca"]
# campur = [1, "dua", True, 3.5]
# bersarang = [
#     [1,2,3,],
#     [1,2,3,],
#     [1,2,3,],
#     [1,2,3,],
#     ]
# # aturan dasar list
# # Urutan DIMULAI dari index 0
# # Bisa diubah
# # Bisa duplikat
# # Bisa  nested(bersarang)
# # urut(ordered)yang berarti urutan yang kita masukkan tidak akan bisa berubah kecuali kita yang merubahnya

# data[0]      # elemen pertama
# data[-1]     # elemen terakhir
# # print(data[1:4])   # slicing
# angka = [0,1,2,3,4,5]
# # print(angka[1:4])   # [1,2,3]
# # print(angka[:3])    # [0,1,2]
# # print(angka[::2])   # [0,2,4]

# # 🔥 METHOD LIST (INI WAJIB HAFAL)

# # 1️⃣ append(x)
# # Tambah 1 item di akhir
# data.append(5)
# # 📥 parameter:
# # x → item bebas (int, str, list, dll)

# # 2️⃣ extend(iterable)
# # Gabung list
# data.extend([6,7,8])
# print(data)
# # 📥 parameter:
# # iterable (list, tuple, set)
# # ❌ beda sama:
# # append([6,7])  # masuk sebagai 1 item

# # 3️⃣ insert(index, x)
# # Sisipkan item
# data.insert(1, 99)
# # 📥 parameter:
# # index → posisi
# # x → nilai

# # 4️⃣ remove(x)
# # Hapus berdasarkan nilai
# data.remove(99)
# # 📥 parameter:
# # x → nilai (harus ada)
# # ❗ error kalau tidak ada

# # 5️⃣ pop(index=-1)
# # Hapus + ambil
# data.pop()
# data.pop(0)
# # 📥 parameter:
# # index (opsional, default terakhir)

# # 6️⃣ clear()
# # Kosongkan list
# data.clear()

# # 7️⃣ index(x, start=0, end=len)
# # Cari index
# data.index(5)
# # 📥 parameter:
# # x → nilai
# # start (opsional)
# # end (opsional)

# # 8️⃣ count(x)
# # Hitung kemunculan
# data.count(5)

# # 9️⃣ sort(key=None, reverse=False)
# # Urutkan
# data.sort()
# data.sort(reverse=True)
# # 📥 parameter:
# # key → fungsi
# # reverse → True / False

# # 🔟 reverse()
# # Balik urutan
# data.reverse()

# MENCARI RATA-RATA
# buat daftar nilai
nilai = [70,75, 54, 67, 65, 43]
# variable total nilai
total_nilai = 0
# variabel length nilai
length_nilai = len(nilai)
# menjumlah kan semua nilai 
for i in nilai:
    total_nilai+= i
# variabel rata-rata
rata_rata = total_nilai / length_nilai
# tampilkan rata-rata
print(rata_rata)

# MENGGANTI NILAI TERENDAH MENJADI NILAI MINIMUM
# daftar nilai
nilai_budi_tolol = [70,75, 54, 67, 65, 43]
# variabel nilai minimum
min_nilai = 70
# cari nilai terendah lalu diganti dengan nilai minimum biar tidak kelihatan tolol muridnya di rapot walaupun terlihat tolol didunia nyata
for index, nilai in enumerate(nilai_budi_tolol):
    if nilai_budi_tolol[index] < min_nilai:
        nilai_budi_tolol[index]= min_nilai
print(nilai_budi_tolol)

# urutkan data
nilai_budi_tolol = [70,75, 54, 67, 65, 43]

nilai_budi_tolol.sort()
print(nilai_budi_tolol)