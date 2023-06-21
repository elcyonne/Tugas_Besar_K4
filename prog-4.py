#WorkSpace zivana

#Kompyutah - Program Jual Beli Perangkat Komputer

#login
def login():
    print("===== Selamat Datang di Program Kompyutah =====")
    print("Anda akan login sebagai:\n1. Administrator\n2. Pembeli\n3. Keluar")

    role = "0"
    max_attempts = 3  # Jumlah maksimal percobaan login
    attempts = 0  # Jumlah percobaan saat ini

    while attempts < max_attempts:
        if role == "0":
            role = input("Pilihan: ")
        elif role == "1":
            username = input("Masukkan username Admin: ")
            password = input("Masukkan password Admin: ")

            # Cek kecocokan username dan password admin
            if username == "admin" and password == "admin":
                print("Selamat datang, Admin!")
                break  # Keluar dari loop jika login berhasil
            else:
                print("Gagal login sebagai Admin!")
                attempts += 1  # Tambah jumlah percobaan
        elif role == "2":
            nama = input("Masukkan nama Anda: ")
            print("\nSelamat datang, {nama}!" .format(nama = nama))
            return nama
            break
        elif role == "3":
            print("Keluar dari program.")
            break
        else:
            role = "0"
            print("Pilihan tidak valid.")

    if attempts == max_attempts:
        print("Anda telah mencapai batas maksimal percobaan.\nProgram akan dihentikan.")

nama = login()

while True:
    print("\nYa")
    break