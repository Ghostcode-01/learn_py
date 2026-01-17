import json

# path file data siswa (JSON)
PATH_DATA = './L_P/D6/PD6/data/siswa.json'

# path file log aktivitas
PATH_DATA_LOG = './L_P/D6/PD6/data/log.txt'


# function untuk mencatat log ke file
def log(message):
    # buka file log dalam mode append (tambah di bawah)
    with open(PATH_DATA_LOG, 'a') as file:
        file.write(message + '\n')


# function untuk membaca data siswa dari file JSON
def load_data():
    try:
        # buka file JSON
        with open(PATH_DATA, 'r') as file_data:
            # load JSON menjadi Python object (list/dict)
            return json.load(file_data)

    # jika file tidak ditemukan
    except FileNotFoundError:
        print('data gak ditemukan')
        return []

    # jika format JSON rusak
    except json.JSONDecodeError:
        print('json rusak')
        return []

    # jika tidak punya izin akses file
    except PermissionError:
        print('gak punya izin akses file')
        return []


# function untuk menyimpan data ke file JSON
def save_data(data):
    try:
        # buka file JSON dalam mode write
        with open(PATH_DATA, 'w') as file_data:
            # simpan data dengan format rapi (indent)
            json.dump(data, file_data, indent=4)

    # jika tidak punya izin menulis file
    except PermissionError:
        print('tidak punya izin menyimpan data')


# function untuk menampilkan seluruh data siswa
def show_data():
    # ambil data dari file
    data = load_data()

    # loop setiap siswa
    for s in data:
        print("\nstudent:", s["student"])

        # loop nilai tiap mapel
        for n in s["score"]:
            print(f"  {n['subject']} : {n['score']}")

        # tampilkan rata-rata dan status
        print("avarage:", s["avarage"])
        print("status:", s["status"])


# function untuk menambah data siswa
def add_student():
    try:
        # load data lama
        data = load_data()

        # input nama siswa
        student_name = input("input the student name: ").strip().capitalize()

        # validasi nama tidak boleh kosong
        if not student_name:
            raise ValueError('nama tidak boleh kosong')

        # list untuk menyimpan nilai
        data_score = []

        # loop input mapel dan nilai
        while True:
            subject = input('input the subject_name: ').strip()

            # stop untuk mengakhiri input nilai
            if subject == 'stop':
                break

            # input nilai dan validasi harus angka
            try:
                score = int(input('input the score: '))
            except ValueError:
                print('nilai harus angka')
                continue

            # simpan mapel dan nilai ke list
            data_score.append({
                'subject': subject,
                'score': score
            })

        # jika tidak ada nilai yang dimasukkan
        if len(data_score) == 0:
            raise ZeroDivisionError("Tidak ada nilai yang dimasukkan")

        # hitung rata-rata nilai
        avarage = sum(i['score'] for i in data_score) / len(data_score)

        # tentukan status kelulusan
        status = 'pass' if avarage >= 75 else 'fail'

        # buat struktur data siswa
        siswa = {
            'student': student_name,
            'score': data_score,
            'avarage': avarage,
            'status': status
        }

        # tambahkan ke data utama
        data.append(siswa)

        # simpan ke file JSON
        save_data(data)

        # catat ke log
        log(f"data nilai {student_name} sudah ditambahkan")
        print("✅ data berhasil ditambahkan")

    # error jika input tidak valid
    except ValueError as ve:
        print("❌ ValueError:", ve)

    # error jika tidak ada nilai
    except ZeroDivisionError as zde:
        print("❌ ZeroDivisionError:", zde)

    # error tipe data
    except TypeError as te:
        print("❌ TypeError:", te)

    # error tak terduga
    except Exception as e:
        print("❌ Error tidak terduga:", e)
