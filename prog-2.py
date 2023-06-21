komputer = {
    "Laptop": [
        ("Lenovo ThinkPad", 10000000, "Intel Core i5, 8GB RAM, 256GB SSD"),
        ("Dell XPS", 15000000, "Intel Core i7, 16GB RAM, 512GB SSD"),
        ("HP Spectre", 12000000, "Intel Core i5, 8GB RAM, 256GB SSD")
    ],
    "PC": [
        ("HP Pavilion", 8000000, "Intel Core i5, 8GB RAM, 1TB HDD"),
        ("Asus ROG", 12000000, "Intel Core i7, 16GB RAM, 1TB SSD"),
        ("Acer Predator", 10000000, "Intel Core i7, 16GB RAM, 512GB SSD")
    ]
}

def tambah_produk(kategori):
    nama_produk = input("Masukkan Nama Produk: ")
    harga = int(input("Masukkan Harga: "))
    spesifikasi = input("Masukkan Spesifikasi: ")
    komputer[kategori].append((nama_produk, harga, spesifikasi))
    print("Produk berhasil ditambahkan.")

def hapus_produk(kategori):
    tampilkan_daftar_produk(kategori)
    nomor_produk = int(input("Masukkan Nomor Produk yang akan dihapus: "))
    if nomor_produk > 0 and nomor_produk <= len(komputer[kategori]):
        produk_terhapus = komputer[kategori].pop(nomor_produk - 1)
        print(f"Produk '{produk_terhapus[0]}' berhasil dihapus.")
    else:
        print("Nomor produk tidak valid.")

def tampilkan_daftar_produk(kategori):
    print(f"Daftar {kategori}:")
    for i, produk in enumerate(komputer[kategori], start=1):
        nama_produk, harga, spesifikasi = produk
        print(f"{i}. {nama_produk} - Rp {harga} - {spesifikasi}")

def pilih_produk(kategori):
    tampilkan_daftar_produk(kategori)
    nomor_produk = int(input("Masukkan Nomor Produk yang dipilih: "))
    if nomor_produk > 0 and nomor_produk <= len(komputer[kategori]):
        produk_terpilih = komputer[kategori][nomor_produk - 1]
        jumlah = int(input("Masukkan Jumlah: "))
        catatan = input("Masukkan Catatan (opsional): ")
        return [(produk_terpilih, jumlah, catatan)]
    else:
        print("Nomor produk tidak valid.")
        return []

def filter_produk(kategori):
    harga_min = int(input("Masukkan Harga Minimum: "))
    harga_max = int(input("Masukkan Harga Maksimum: "))
    produk_terfilter = [produk for produk in komputer[kategori] if harga_min <= produk[1] <= harga_max]
    if len(produk_terfilter) == 0:
        print(f"Tidak ada {kategori} dalam rentang harga tersebut.")
    else:
        print(f"Daftar {kategori} (Harga: {harga_min} - {harga_max}):")
        for i, produk in enumerate(produk_terfilter, start=1):
            nama_produk, harga, spesifikasi = produk
            print(f"{i}. {nama_produk} - Rp {harga} - {spesifikasi}")

def cari_produk(kategori):
    kata_kunci = input("Masukkan Kata Kunci: ")
    produk_terfilter = [produk for produk in komputer[kategori] if kata_kunci.lower() in produk[0].lower()]
    if len(produk_terfilter) == 0:
        print(f"Tidak ada {kategori} yang cocok dengan kata kunci '{kata_kunci}'.")
    else:
        print(f"Daftar {kategori} (Pencarian: '{kata_kunci}'):")
        for i, produk in enumerate(produk_terfilter, start=1):
            nama_produk, harga, spesifikasi = produk
            print(f"{i}. {nama_produk} - Rp {harga} - {spesifikasi}")

def tampilkan_keranjang():
    if len(keranjang) == 0:
        print("Keranjang belanja kosong.")
    else:
        print("Rangkuman Keranjang Belanja:")
        total_harga = 0
        for i, (produk, jumlah, catatan) in enumerate(keranjang, start=1):
            nama_produk, harga, _ = produk
            subtotal = harga * jumlah
            total_harga += subtotal
            print(f"{i}. {nama_produk} - {jumlah} - {catatan} - Rp {subtotal}")
        print(f"Total Harga: Rp {total_harga}")

def checkout():
    if len(keranjang) == 0:
        print("Keranjang belanja kosong. Tidak ada yang bisa di-checkout.")
    else:
        tampilkan_keranjang()
        total_harga = sum(harga * jumlah for produk, jumlah, _ in keranjang)
        print("Total yang harus dibayar:", total_harga)
        konfirmasi = input("Apakah Anda yakin ingin melakukan checkout? (ya/tidak) ")
        if konfirmasi.lower() == "ya":
            print("Checkout berhasil. Terima kasih telah berbelanja!")
            keranjang.clear()
        else:
            print("Checkout dibatalkan.")

def tampilkan_menu_penjual():
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    if username == "admin" and password == "admin":
        while True:
            print("=== Menu Penjual ===")
            print("1. Tampilkan Daftar Produk")
            print("2. Tambah Produk")
            print("3. Hapus Produk")
            print("4. Kembali")
            pilihan_menu = input("Masukkan Pilihan: ")

            if pilihan_menu == "1":
                for kategori in komputer:
                    tampilkan_daftar_produk(kategori)
            elif pilihan_menu == "2":
                kategori = input("Masukkan Kategori Produk: ")
                if kategori in komputer:
                    tambah_produk(kategori)
                else:
                    print("Kategori produk tidak valid.")
            elif pilihan_menu == "3":
                kategori = input("Masukkan Kategori Produk: ")
                if kategori in komputer:
                    hapus_produk(kategori)
                else:
                    print("Kategori produk tidak valid.")
            elif pilihan_menu == "4":
                return
            else:
                print("Pilihan tidak valid!")
    else:
        print("Username atau password salah.")

def tampilkan_menu_pembeli():
    while True:
        print("=== Menu Pembeli ===")
        print("1. Tampilkan Daftar Produk")
        print("2. Pilih Produk")
        print("3. Filter Produk Berdasarkan Harga")
        print("4. Cari Produk")
        print("5. Tampilkan Keranjang Belanja")
        print("6. Checkout")
        print("7. Kembali")
        pilihan_menu = input("Masukkan Pilihan: ")

        if pilihan_menu == "1":
            for kategori in komputer:
                tampilkan_daftar_produk(kategori)
        elif pilihan_menu == "2":
            kategori = input("Masukkan Kategori Produk: ")
            if kategori in komputer:
                produk_terpilih = pilih_produk(kategori)
                if len(produk_terpilih) > 0:
                    keranjang.extend(produk_terpilih)
            else:
                print("Kategori produk tidak valid.")
        elif pilihan_menu == "3":
            kategori = input("Masukkan Kategori Produk: ")
            if kategori in komputer:
                filter_produk(kategori)
            else:
                print("Kategori produk tidak valid.")
        elif pilihan_menu == "4":
            kategori = input("Masukkan Kategori Produk: ")
            if kategori in komputer:
                cari_produk(kategori)
            else:
                print("Kategori produk tidak valid.")
        elif pilihan_menu == "5":
            tampilkan_keranjang()
        elif pilihan_menu == "6":
            checkout()
        elif pilihan_menu == "7":
            return
        else:
            print("Pilihan tidak valid!")

keranjang = []

while True:
    print("=== Aplikasi Jual Beli Komputer ===")
    print("1. Menu Penjual")
    print("2. Menu Pembeli")
    print("3. Keluar")
    pilihan_menu = input("Masukkan Pilihan: ")

    if pilihan_menu == "1":
        tampilkan_menu_penjual()
    elif pilihan_menu == "2":
        tampilkan_menu_pembeli()
    elif pilihan_menu == "3":
        break
    else:
        print("Pilihan tidak valid!")
