import json

# simpan data task ke file JSON
def save_file(data):
    with open('./L_P/D8/backend/database.json', 'w') as f:
        json.dump(data, f, indent=4)


# load data task dari file JSON
def load_file():
    try:
        with open('./L_P/D8/backend/database.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        # jika file belum ada
        print('data gak ada')
        return []


# tambah task baru
def tambah_task():
    data = load_file()

    # input deskripsi task
    task = input('masukkan deskripsi tugas: ')

    # struktur data task
    data_tugas = {
        "Description": task,
        "Done": 'false'
    }

    # tambahkan ke list
    data.append(data_tugas)

    # simpan ke file
    save_file(data)


# hapus task berdasarkan indeks
def hapus_task():
    data = load_file()

    try:
        indeks_delete = int(input('masukkan indeks yang akan dihapus: '))
    except:
        print('harus angka')
        return

    # jika data kosong
    if not data:
        print("belum ada task woii")
        return

    # validasi indeks
    if indeks_delete <= 0 or indeks_delete > len(data):
        print('angka tidak valid')
        return

    # hapus task
    del data[indeks_delete - 1]

    # simpan ulang
    save_file(data)


# tampilkan semua task
def tampilkan_task():
    data = load_file()

    if not data:
        print('task belum ada')
        return

    # loop task dan tampilkan status
    for i, d in enumerate(data):
        status = "✔" if d.get("Done")=="true" else "✘"
        print(f"{i+1}. {d['Description']} [{status}]")
