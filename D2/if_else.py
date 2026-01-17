# terima input nama
nama = input("masukkan nama: ")
# terima input umur
umur = int(input('masukkan umur: '))
# variabel hasil
hasil = ''
# cek, jika umur nya dibawah 18 maka muda, jika diatas 18 maka remaja jika diatas 30 tua
if umur < 18:
    hasil ='anda muda'
elif umur <30:
    hasil ='anda remaja'
else:
    hasil = 'anda tua'

# print hasil
print(hasil)
