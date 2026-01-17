import time

# function untuk load konfigurasi aplikasi
def load_config(**setting):
    # tampilkan semua konfigurasi
    for k, v in setting.items():
        print(f'{k} : {v}')
        time.sleep(0.5)

    print('Welcome to CLI')
