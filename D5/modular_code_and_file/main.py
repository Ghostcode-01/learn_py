# import file kalkulator.py
# artinya kita pakai function yang sudah kita buat di file lain
import kalkulator

# panggil function tambah dari module kalkulator
# semua angka akan dijumlahkan
print(kalkulator.tambah(2, 3, 45, 6, 5, 6, 3, 4, 53255))

# panggil function kurang
# pengurangan dilakukan dari angka pertama lalu berurutan
print(kalkulator.kurang(2, 3, 45, 6, 5, 6, 3, 4, 53255))

# panggil function kali
# semua angka akan dikalikan satu per satu
print(kalkulator.kali(2, 3, 45, 6, 5, 6, 3, 4, 53255))

# panggil function bagi
# pembagian dilakukan berurutan dan dicek agar tidak ada pembagian dengan nol
print(kalkulator.bagi(7867, 5885, 56, 5, 56, 56))
