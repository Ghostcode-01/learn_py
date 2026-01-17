# # 1. masukkan data
# data = [
#     {
#     'buah': 'jeruk',
#     'harga': 100000,
#     },
#     {
#     'buah': 'nanas',
#     'harga': 200000,
#     },
#     {
#     'buah': 'jeruk',
#     'harga': 300000,
#     } 
# ]
# # 2. tampilkan menu di terminal
# for fruit in data:
#     print(fruit['buah'],'harga:', fruit['harga'])

# # buat variabel keranjang untuk menampung pesanan
# keranjang= []
# # lalu buat looping pencarian
# while True:
#     #terima input dari user
#     pesanan = input('mau beli apa: ')
#     jumlah = int(input('jumlah: '))
#     # variabel buat validasi apakah buah nya ada atau tidak
#     ditemukan = False
#     total = 0
#     for fruit in data:
#         if fruit['buah']==pesanan:
#             ditemukan = True
#             keranjang.append({
#                 'buah': fruit['buah'],
#                 'harga': fruit['harga'],
#                 'jumlah': jumlah
#             })
#             print('sudah ditambahkan')
#             break
#     if not ditemukan:
#         print('masukkan buah yang ada di menu')
#         pesanan
#     lanjut = input("Ada lagi? (y/n): ").lower()
#     if lanjut == 'y':
#                 pesanan
#     else:
#         print("\n=== STRUK ===")
#         for item in keranjang:
#             subtotal = item['harga'] * item['jumlah']
#             total = total + subtotal
#             print(item['buah'], item['jumlah'], "x", item['harga'], "=", subtotal)
#             break

# SISTEM TARIF PARKIR SEDERHANA
# Data parkir disimpan dalam bentuk jam parkir
# Jika nilai 0, artinya kendaraan sudah bayar dan keluar

data_parkir = [1, 2, 3, 4, 7, 8, 9]

# Batas maksimal jam parkir normal
maks_jam = 5

# Tarif parkir per jam
tarif_parkir = 2000

# Total pendapatan parkir
pendapatan = 0

# Menghitung sudah berapa kali loop berjalan
loop_count = 0

# Selama masih ada kendaraan di parkiran
while len(data_parkir) > 0:
    loop_count += 1

    # Tampilkan kondisi parkir terbaru
    print("\nData Parkir Sekarang:", data_parkir)

    # Hapus kendaraan yang sudah keluar (jam = 0)
    data_parkir_baru = []
    for jam in data_parkir:
        if jam != 0:
            data_parkir_baru.append(jam)
    data_parkir = data_parkir_baru

    # Setiap 3 kali loop, semua jam parkir bertambah 1
    if loop_count % 3 == 0:
        print("⏱️ Semua jam parkir bertambah 1")
        for i in range(len(data_parkir)):
            data_parkir[i] += 1

    # Input kendaraan yang ingin keluar
    keluar = input("Masukkan indeks kendaraan yang keluar (Enter jika tidak ada): ")

    # Jika ada kendaraan keluar
    if keluar != "":
        index = int(keluar)

        # Cek apakah indeks valid
        if index < len(data_parkir):
            jam = data_parkir[index]

            # Hitung biaya parkir
            if jam > maks_jam:
                bayar = jam * tarif_parkir * 2
            else:
                bayar = jam * tarif_parkir

            pendapatan += bayar
            data_parkir[index] = 0
            print(f"💸 Bayar: {bayar}")
        else:
            print("❌ Nomor parkir tidak valid")

print("\n🏁 Parkiran kosong")
print("Total pendapatan:", pendapatan)
