#login
def login():
    role = input("Apakah Anda penjual atau pembeli? (P/PB): ")

    max_attempts = 3  # Jumlah maksimal percobaan login
    attempts = 0  # Jumlah percobaan saat ini

    while attempts < max_attempts:
        if role.lower() == "p":
            username = input("Masukkan username penjual: ")
            password = input("Masukkan password penjual: ")

            # Cek kecocokan username dan password penjual
            if username == "admin" and password == "12345":
                print("Selamat datang, penjual!")
                break  # Keluar dari loop jika login berhasil
            else:
                print("Gagal login sebagai penjual!")

        elif role.lower() == "pb":
            username = input("Masukkan username pembeli: ")
            password = input("Masukkan password pembeli: ")

            # Cek kecocokan username dan password pembeli
            if username == "user" and password == "54321":
                print("Selamat datang, pembeli!")
                break  # Keluar dari loop jika login berhasil
            else:
                print("Gagal login sebagai pembeli!")

        else:
            print("Peran yang dimasukkan tidak valid.")

        attempts += 1  # Tambah jumlah percobaan

    if attempts == max_attempts:
        print("Anda telah mencapai batas maksimal percobaan. Silakan coba lagi nanti.")
