a = 10
b = 3

print(a + b)   # tambah
print(a - b)   # kurang
print(a * b)   # kali
print(a / b)   # bagi
print(a // b)  # pembagian bulat
print(a % b)   # sisa bagi
print(a ** b)  # pangkat

# input angka pertama dari user
angka_STR1 = input('masukkan angka pertama : ')
# input angka kedua dari user

angka_STR2 = input('masukkan angka kedua : ')

angka_pertama = int(angka_STR1)
angka_kedua = int(angka_STR2)

# input operator dari user (operator yang didukung +  -  *  /  %  **)
hasil =0
operator =  input('masukkan +  -  *  /  %  **:')

# buat sebuah if/elif/else
if(operator == '+'):
    hasil= angka_pertama + angka_kedua 
elif (operator == '-'):
    hasil = angka_pertama - angka_kedua
elif (operator =='*'):
    hasil = angka_pertama * angka_kedua
elif (operator == '/'):
    hasil = angka_pertama / angka_kedua
elif (operator == '%'):
    hasil = angka_pertama % angka_kedua
elif (operator == '**'):
    hasil = angka_pertama ** angka_kedua


# lalu tampilkan output 
print(hasil)