# import function load_file dari task_utils
from task_utils import load_file


# function untuk menghitung persentase task yang selesai
def hitung_progress():
    data = load_file()

    # jika data kosong, progress 0%
    if not data:
        return 0

    # hitung task yang sudah selesai
    selesai =0
    for i in data :
        if i.get("Done") == "true":
            selesai+=1

    # hitung persentase
    return (selesai / len(data)) * 100
