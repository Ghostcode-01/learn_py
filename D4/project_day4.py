# SISTEM NILAI SISWA SEDERHANA
# Data siswa disimpan menggunakan list dan dictionary

all_siswa = []

# Variabel untuk menjalankan program terus-menerus
start = True

while start:
    # Menu pilihan program
    command = int(input(
        "Pilih menu:\n"
        "1. Masukkan data siswa dan nilai\n"
        "2. Tampilkan ranking siswa\n"
        "3. Keluar\n"
        "Input: "
    ))

    # MENU 1: Input data siswa
    if command == 1:
        nama_siswa = input("Masukkan nama siswa: ")

        # Menyimpan nilai setiap mata pelajaran
        nilai_list = []

        # Loop untuk input nilai per mapel
        while True:
            m_v_siswa = input("Masukkan mapel dan nilai (ketik 'selesai' jika sudah): ")

            if m_v_siswa == "selesai":
                break

            mapel, nilai = m_v_siswa.split()
            nilai = int(nilai)

            nilai_list.append({
                "mapel": mapel,
                "nilai": nilai
            })

        # Hitung total dan rata-rata nilai
        total = 0
        for n in nilai_list:
            total += n["nilai"]

        rata_rata = total / len(nilai_list)

        # Tentukan status kelulusan
        status = "lulus" if rata_rata >= 75 else "gak lulus"

        # Simpan data siswa ke list utama
        all_siswa.append({
            "nama": nama_siswa,
            "nilai": nilai_list,
            "rata_rata": rata_rata,
            "status": status
        })

    # MENU 2: Tampilkan ranking siswa
    elif command == 2:
        ranking = sorted(
            all_siswa,
            key=lambda s: s["rata_rata"],
            reverse=True
        )

        print("\n=== RANKING SISWA ===")
        for i, siswa in enumerate(ranking, start=1):
            print(
                f"{i}. {siswa['nama']} | "
                f"Rata-rata: {siswa['rata_rata']} | "
                f"Status: {siswa['status']}"
            )

    # MENU 3: Keluar dari program
    elif command == 3:
        start = False

print("Program selesai")
