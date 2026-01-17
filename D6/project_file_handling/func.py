import json
def tulis_log(pesan):
    with open('./learn_python/day6/project_file_handling/data.txt', "a") as f:
        f.write(pesan + '\n')

def load_data():
    with open("data_siswa.json", "r") as f:
        return json.load(f)

def save_data(data):
    with open("data_siswa.json", "w") as f:
        json.dump(data, f, indent=4)

def tambah_siswa():
    data = load_data()

    nama = input("Nama siswa: ")
    nilai = []

    while True:
        mapel = input("Mapel (ketik stop untuk selesai): ")
        if mapel == "stop":
            break

        n = int(input("Nilai: "))
        nilai.append({
            "mapel": mapel,
            "nilai": n
        })

    rata = sum(i["nilai"] for i in nilai) / len(nilai)
    status = "lulus" if rata >= 75 else "gak lulus"

    siswa = {
        "nama": nama,
        "nilai": nilai,
        "rata_rata": rata,
        "status": status
    }

    data.append(siswa)
    save_data(data)

    tulis_log(f"Tambah siswa: {nama}")
