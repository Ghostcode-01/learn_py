# function tambah
# menerima banyak angka sekaligus menggunakan *args
def tambah(*nilai):
    # jika tidak ada angka yang dikirim, kembalikan 0
    if not nilai:
        return 0

    # ambil angka pertama sebagai nilai awal
    total = nilai[0]

    # loop sisa angka lalu tambahkan ke total
    for a in nilai[1:]:
        total += a

    # kembalikan hasil penjumlahan
    return total


# function kurang
# pengurangan dilakukan secara berurutan
def kurang(*nilai):
    # jika tidak ada input, hasilnya 0
    if not nilai:
        return 0

    # angka pertama dijadikan nilai awal
    total = nilai[0]

    # kurangi total dengan angka berikutnya satu per satu
    for a in nilai[1:]:
        total -= a

    # kembalikan hasil pengurangan
    return total


# function kali
# mengalikan semua angka yang dikirim
def kali(*nilai):
    # jika tidak ada input, hasilnya 0
    if not nilai:
        return 0

    # ambil angka pertama sebagai nilai awal
    total = nilai[0]

    # kalikan total dengan angka berikutnya
    for a in nilai[1:]:
        total *= a

    # kembalikan hasil perkalian
    return total


# function bagi
# pembagian dilakukan secara berurutan
def bagi(*nilai):
    # jika tidak ada input, hasilnya 0
    if not nilai:
        return 0

    # angka pertama dijadikan nilai awal
    total = nilai[0]

    # lakukan pembagian satu per satu
    for a in nilai[1:]:
        # cek agar tidak terjadi pembagian dengan nol
        if a == 0:
            return "Error: pembagian dengan 0"

        total /= a

    # kembalikan hasil pembagian
    return total
