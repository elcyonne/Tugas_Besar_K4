#Workspace - Gibranr try error
menu = {
    "Laptop": [],
    "Keyboard": [],
    "Mouse": [],
    "Monitor": [],
    "RAM": [],
    "Graphic Card": [],
    "Processor": [],
    "Kembali": []
}

keranjang = []

def tampilkan_daftar_menu(kategori):
    if len(menu[kategori]) == 0:
        print(f"Daftar Menu {kategori} kosong.")
    else:
        print(f"Daftar Menu {kategori}:")
        print("-----------------------------------------")
        print("| No. | Nama Produk  | Harga | Spesifikasi |")
        print("-----------------------------------------")
        for i, produk in enumerate(menu[kategori], start=1):
            nama_produk, harga, spesifikasi = produk
            print(f"| {i:3} | {nama_produk:12} | {harga:5} | {spesifikasi:11} |")
        print("-----------------------------------------")

def pilih_menu(kategori):
    nomor_produk = int(input("Masukkan Nomor Produk yang dipilih: "))
    if nomor_produk > 0 and nomor_produk <= len(menu[kategori]):
        jumlah = int(input("Masukkan Jumlah: "))
        catatan = input("Masukkan Catatan: ")
        produk = menu[kategori][nomor_produk - 1]
        return [(produk, jumlah, catatan)]
    else:
        print("Nomor produk tidak valid.")
        return []

def filter_menu(kategori):
    filter_harga = int(input("Masukkan Harga Maksimum: "))
    produk_terfilter = [produk for produk in menu[kategori] if produk[1] <= filter_harga]
    if len(produk_terfilter) == 0:
        print(f"Tidak ada produk {kategori} dengan harga di bawah {filter_harga}.")
    else:
        print(f"Daftar Menu {kategori} (Harga di bawah {filter_harga}):")
        print("-----------------------------------------")
        print("| No. | Nama Produk  | Harga | Spesifikasi |")
        print("-----------------------------------------")
        for i, produk in enumerate(produk_terfilter, start=1):
            nama_produk, harga, spesifikasi = produk
            print(f"| {i:3} | {nama_produk:12} | {harga:5} | {spesifikasi:11} |")
        print("-----------------------------------------")

def cari_menu(kategori):
    kata_kunci = input("Masukkan Kata Kunci: ")
    produk_terfilter = [produk for produk in menu[kategori] if kata_kunci.lower() in produk[0].lower()]
    if len(produk_terfilter) == 0:
        print(f"Tidak ada produk {kategori} yang cocok dengan kata kunci '{kata_kunci}'.")
    else:
        print(f"Daftar Menu {kategori} (Pencarian: '{kata_kunci}'):")
        print("-----------------------------------------")
        print("| No. | Nama Produk  | Harga | Spesifikasi |")
        print("-----------------------------------------")
        for i, produk in enumerate(produk_terfilter, start=1):
            nama_produk, harga, spesifikasi = produk
            print(f"| {i:3} | {nama_produk:12} | {harga:5} | {spesifikasi:11} |")
        print("-----------------------------------------")

def tampilkan_keranjang():
    if len(keranjang) == 0:
        print("Keranjang belanja kosong.")
    else:
        print("Rangkuman Keranjang Belanja:")
        print("---------------------------------------------")
        print("| No. | Nama Produk  | Jumlah | Catatan | Harga |")
        print("---------------------------------------------")
        total_harga = 0
        for i, (produk, jumlah, catatan) in enumerate(keranjang, start=1):
            nama_produk, harga, _ = produk
            subtotal = harga * jumlah
            total_harga += subtotal
            print(f"| {i:3} | {nama_produk:12} | {jumlah:6} | {catatan:7} | {subtotal:5} |")
        print("---------------------------------------------")
        print(f"Total Harga: {total_harga}")

def checkout():
    if len(keranjang) == 0:
        print("Keranjang belanja kosong. Tidak ada yang bisa di-checkout.")
    else:
        tampilkan_keranjang()
        print("---------------------------------------------")
        total_harga = sum(harga * jumlah for produk, jumlah, _ in keranjang)
        print("Total yang harus dibayar:", total_harga)
        print("---------------------------------------------")
        konfirmasi = input("Apakah Anda ingin melakukan pembayaran? (y/n): ")
        if konfirmasi.lower() == "y":
            print("Pembayaran berhasil.")
            keranjang.clear()
        else:
            print("Pembayaran dibatalkan.")

def tambah_produk(kategori):
    nama_produk = input("Masukkan Nama Produk: ")
    harga = int(input("Masukkan Harga: "))
    spesifikasi = input("Masukkan Spesifikasi: ")
    produk = (nama_produk, harga, spesifikasi)
    menu[kategori].append(produk)
    print(f"Produk '{nama_produk}' telah ditambahkan ke menu {kategori}.")

def hapus_produk(kategori):
    tampilkan_daftar_menu(kategori)
    nomor_produk = int(input("Masukkan Nomor Produk yang ingin dihapus: "))
    if nomor_produk > 0 and nomor_produk <= len(menu[kategori]):
        nama_produk, _, _ = menu[kategori][nomor_produk - 1]
        del menu[kategori][nomor_produk - 1]
        print(f"Produk '{nama_produk}' telah dihapus dari menu {kategori}.")
    else:
        print("Nomor produk tidak valid.")

def tampilkan_menu_seller():
    while True:
        print("=== Menu Penjual ===")
        print("1. Tampilkan Daftar Menu")
        print("2. Tambah Produk")
        print("3. Hapus Produk")
        print("4. Kembali")
        pilihan_menu = input("Masukkan Pilihan: ")

        if pilihan_menu == "1":
            for kategori in menu:
                tampilkan_daftar_menu(kategori)
        elif pilihan_menu == "2":
            kategori = input("Masukkan Kategori Produk: ")
            if kategori in menu:
                tambah_produk(kategori)
            else:
                print("Kategori produk tidak valid.")
        elif pilihan_menu == "3":
            kategori = input("Masukkan Kategori Produk: ")
            if kategori in menu:
                hapus_produk(kategori)
            else:
                print("Kategori produk tidak valid.")
        elif pilihan_menu == "4":
            return
        else:
            print("Pilihan tidak valid!")

def tampilkan_menu_buyer():
    while True:
        print("=== Menu Pembeli ===")
        print("1. Tampilkan Daftar Menu")
        print("2. Pilih Produk")
        print("3. Filter Produk Berdasarkan Harga")
        print("4. Cari Produk")
        print("5. Tampilkan Keranjang Belanja")
        print("6. Checkout")
        print("7. Kembali")
        pilihan_menu = input("Masukkan Pilihan: ")

        if pilihan_menu == "1":
            for kategori in menu:
                tampilkan_daftar_menu(kategori)
        elif pilihan_menu == "2":
            kategori = input("Masukkan Kategori Produk: ")
            if kategori in menu:
                produk_terpilih = pilih_menu(kategori)
                keranjang.extend(produk_terpilih)
            else:
                print("Kategori produk tidak valid.")
        elif pilihan_menu == "3":
            kategori = input("Masukkan Kategori Produk: ")
            if kategori in menu:
                filter_menu(kategori)
            else:
                print("Kategori produk tidak valid.")
        elif pilihan_menu == "4":
            kategori = input("Masukkan Kategori Produk: ")
            if kategori in menu:
                cari_menu(kategori)
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

def main_menu():
    while True:
        print("=== Aplikasi Penjualan ===")
        print("1. Menu Penjual")
        print("2. Menu Pembeli")
        print("3. Keluar")
        pilihan_menu = input("Masukkan Pilihan: ")

        if pilihan_menu == "1":
            tampilkan_menu_seller()
        elif pilihan_menu == "2":
            tampilkan_menu_buyer()
        elif pilihan_menu == "3":
            return
        else:
            print("Pilihan tidak valid!")

main_menu()

