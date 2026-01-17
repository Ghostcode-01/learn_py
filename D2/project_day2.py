# # terima input nama barang
# nama_barang = input('masukkan nama barang: ')
# # terima input harga
# harga = int(input('masukkan harga: '))
# # jumlah barang
# jumlah = int(input("masukkan jumlah barang: "))
# #hitung total 
# total = harga * jumlah
# #diskon
# diskon = 10/100
# #jika total > 100.000 maka diskon 10%
# if total > 100000:
#     total = total - (total * diskon)
# # tampilkan total
# print(total)

# 1. Minta user memasukkan harga barang
harga_barang = int(input('masukkan harga barang: '))
# 2. Minta user memasukkan jumlah barang
jumlah_barang = int(input('masukkan jumlah barang: '))
# 3. Hitung total harga (harga × jumlah)
total_harga = harga_barang * jumlah_barang
# 4. Jika total >= 100000, beri diskon dan tampilkan
if total_harga >=100000:
    print('anda dapat diskon 10%')
# 5. buat variabel discount
    diskon = 10 / 100
# 6. buat variabel total harga setelah diskon
    total_setelah_diskon = total_harga - (total_harga * diskon)
# 7. tampilkan harga nya
    print(total_setelah_diskon)
# 8. Jika tidak, tampilkan total normal
else :
    print(total_harga)
