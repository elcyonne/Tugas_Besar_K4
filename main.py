# Kelompok 4: POLARIS
# Kompyuta - Program Jual Beli Perangkat Komputer dan Perakitan Komputer

# Prosedur & Fungsi
import os


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def login():
    print("===== Selamat Datang di Program Kompyuta =====")
    print("Anda akan login sebagai:\n1. Administrator\n2. Pembeli\n3. Keluar")

    role = "0"
    max_attempts = 3  # Jumlah maksimal percobaan login
    attempts = 0      # Jumlah percobaan saat ini

    while attempts < max_attempts:
        if role == "0":
            role = input("Pilihan: ")
        elif role == "1":
            username = input("Masukkan username Admin: ")
            password = input("Masukkan password Admin: ")

            # Cek kecocokan username dan password admin
            if username == "admin" and password == "admin":
                clear()
                print("Selamat datang, Admin!")
                return role         # Keluar dari loop jika login berhasil
            else:
                print("Gagal login sebagai Admin!\n")
                attempts += 1       # Tambah jumlah percobaan
        elif role == "2":
            nama = input("Masukkan nama Anda: ")
            clear()
            print(f"Selamat datang, {nama}!")
            return nama
        elif role == "3":
            print("Keluar dari program.")
            return "keluar"
        else:
            role = "0"
            print("Pilihan tidak valid.\n")

    if attempts == max_attempts:
        print("Anda telah mencapai batas maksimal percobaan.\nProgram akan dihentikan.")
        return "keluar"


def cek_produk():
    # Cek file produk. Kalau tidak ada, buat file dari komponen tersebut
    import os
    if not os.path.exists("./Produk"):
        os.mkdir("./Produk")
    if not os.path.exists("./Pembelian"):
        os.mkdir("./Pembelian")
    from os.path import exists
    for i in range(len(file_produk)):
        file_exist = exists('./Produk/' + file_produk[i])
        if file_exist == False:
            with open("./Produk/" + file_produk[i], "w") as txt_file:
                for line in produk_awal[i]:
                    txt_file.write(" ".join(line) + "\n")
    # Tambah produk dari masing masing komponen ke array 3D produk
    for j in range(len(file_produk)):
        produk.append(ambil_array_produk(j + 1))


def ambil_array_produk(komponen, sumber_file=True):
    # komponen = 1-cpu, 2-motherboard, 3-cpucooler, 4-vga_card, 5-ram, 6-psu, 7-storage, 8-case, 9-fan
    arr = []
    if sumber_file:
        # Baca file produk dan konversi produk tersebut menjadi array 2D sesuai dengan komponen yang dipilih
        with open('./Produk/' + file_produk[komponen-1], "r") as file:
            for line in file:
                arr.append(line.split())
        # Ganti _ menjadi <spasi> di setiap elemen array produk sesuai dengan komponen yang dipilih
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                ganti = arr[i][j].replace("_", " ")
                arr[i][j] = ganti
    else:
        # Baca produk dari array 3D produk
        arr = produk[komponen - 1]
    return arr


def tulis_produk(komponen):
    # Tulis produk dari komponen terkait ke file dari komponen tersebut
    # array_produk = ["Komponen", "Nama Produk", "Harga", "Spek Kunci"]
    produk_lama = produk[komponen-1]
    # Ganti <spasi> menjadi _ di setiap elemen array produk sesuai dengan komponen yang dipilih
    for i in range(len(produk_lama)):
        for j in range(len(produk_lama[i])):
            ganti = produk_lama[i][j].replace(" ", "_")
            produk_lama[i][j] = ganti
    # Tulis produk dari komponen yang dipilih ke file terkait
    with open('./Produk/' + file_produk[komponen-1], "w") as txt_file:
        for line in produk_lama:
            txt_file.write(" ".join(line) + "\n")
    # Ganti _ menjadi <spasi> di setiap elemen array produk sesuai dengan komponen yang dipilih
    for i in range(len(produk_lama)):
        for j in range(len(produk_lama[i])):
            ganti = produk_lama[i][j].replace("_", " ")
            produk_lama[i][j] = ganti


def tambah_produk(komponen, array_produk):
    # array_produk = ["Komponen", "Nama Produk", "Harga", "Spek Kunci"]
    produk_lama = ambil_array_produk(komponen, False)
    produk_lama.append(array_produk)
    # Ganti <spasi> menjadi _ di setiap elemen array produk sesuai dengan komponen yang dipilih
    for i in range(len(produk_lama)):
        for j in range(len(produk_lama[i])):
            ganti = produk_lama[i][j].replace(" ", "_")
            produk_lama[i][j] = ganti
    # Tulis produk dari komponen yang dipilih ke file terkait
    with open('./Produk/' + file_produk[komponen - 1], "w") as txt_file:
        for line in produk_lama:
            txt_file.write(" ".join(line) + "\n")
    # Ganti array 2D komponen terkait dengan yang sudah diperbarui
    for k in range(len(produk[komponen - 1])):
        for l in range(len(produk[komponen - 1][k])):
            ganti = produk[komponen - 1][k][l].replace("_", " ")
            produk[komponen - 1][k][l] = ganti
    produk[komponen - 1] = ambil_array_produk(komponen, False)


def hapus_produk(komponen, nomor):
    # nomor = nomor indeks di array produk
    nomor -= 1
    produk_lama = ambil_array_produk(komponen, False)
    produk_lama.pop(nomor)
    # Ganti <spasi> menjadi _ di setiap elemen array produk sesuai dengan komponen yang dipilih
    for i in range(len(produk_lama)):
        for j in range(len(produk_lama[i])):
            ganti = produk_lama[i][j].replace(" ", "_")
            produk_lama[i][j] = ganti
    # Tulis produk dari komponen yang dipilih ke file terkait
    with open('./Produk/' + file_produk[komponen - 1], "w") as txt_file:
        for line in produk_lama:
            txt_file.write(" ".join(line) + "\n")
    # Ganti array 2D komponen terkait dengan yang sudah diperbarui
    for k in range(len(produk[komponen - 1])):
        for l in range(len(produk[komponen - 1][k])):
            ganti = produk[komponen - 1][k][l].replace("_", " ")
            produk[komponen - 1][k][l] = ganti
    produk[komponen - 1] = ambil_array_produk(komponen, False)


def harga_keranjang():
    # Ganti tipe data dari harga yang ada di array keranjang menjadi integer-string dan hitung harga total
    total_harga = 0
    for i in range(len(keranjang)):
        keranjang[i][3] = int(keranjang[i][3])
        total_harga += keranjang[i][0] * keranjang[i][3]
        keranjang[i][3] = str(keranjang[i][3])
    return total_harga


def file_pembelian():
    # Buat file pembelian berdasarkan keranjang
    import datetime
    waktu = datetime.datetime.now()
    nama_file = nama + " " + str(waktu.year) + "-" + str(waktu.month) + "-" + str(waktu.day) + " " + str(
        waktu.hour) + "-" + str(waktu.minute) + "-" + str(waktu.second) + ".txt"
    for i in range(len(keranjang)):
        keranjang[i][0] = str(keranjang[i][0])
    with open('./Pembelian/' + nama_file, "w") as txt_file:
        for line in keranjang:
            txt_file.write(" ".join(line) + "\n")
    clear()
    print("File pembelian Anda berhasil dibuat."
          "\nKeranjang dikosongkan kembali.")


def tampilkan_daftar_produk(komponen, custom=False):
    # komponen = nomor_komponen (custom = array 2D)
    if custom:
        for i in range(len(komponen)):
            print(
                f"{i + 1}. {komponen[i][0]} - {komponen[i][1]} - Rp.{komponen[i][2]} - {komponen[i][3]}")
    else:
        print(f"Daftar {produk[komponen - 1][0][0]}:")
        for i in range(len(produk[komponen - 1])):
            print(
                f"{i + 1}. {produk[komponen - 1][i][0]} - {produk[komponen - 1][i][1]} - "
                f"Rp.{produk[komponen - 1][i][2]} - {produk[komponen - 1][i][3]}")


def urutkan_produk(komponen, indeks_kolom, descending=False, admin=True):
    # Urutkan produk dari komponen terkait berdasarkan kolom yang dipilih
    # indeks_kolom = 1-Nama produk, 2-Harga, 3-Spek_kunci
    arr = produk[komponen - 1]
    if indeks_kolom == 2:
        for i in range(len(arr)):
            arr[i][2] = int(arr[i][2])
        sorted_arr = sorted(arr, key=lambda x: x[indeks_kolom], reverse=descending)
        for j in range(len(arr)):
            arr[j][2] = str(arr[j][2])
    else:
        sorted_arr = sorted(arr, key=lambda x: x[indeks_kolom], reverse=descending)
    produk[komponen - 1] = sorted_arr
    if admin:
        tulis_produk(komponen)


def cari_produk(kunci):
    # Cari produk dengan kata kunci dan mengembalikan hasilnya dengan array 2D jika ada, -1 jika tidak ada
    # kunci = string kata yang ingin dicari
    hasil = []
    for i in range(len(produk)):
        for j in range(len(produk[i])):
            for k in range(len(produk[i][j])):
                kata = produk[i][j][k].lower()
                valid = kata.find(kunci)
                if valid != -1:
                    if len(hasil) == 0:
                        hasil.append(produk[i][j])
                    else:
                        if hasil[len(hasil)-1] != produk[i][j]:
                            hasil.append(produk[i][j])
    if len(hasil) == 0:
        return -1
    else:
        return hasil


def tampilkan_keranjang():
    if len(keranjang) > 0:
        for i in range(len(keranjang)):
            if len(keranjang[i]) == 4:
                print(f"{i + 1}. {keranjang[i][0]} {keranjang[i][1]} - Rp.{keranjang[i][2]} - {keranjang[i][3]}")
            else:
                print(f"{i + 1}. {keranjang[i][0]} {keranjang[i][1]} {keranjang[i][2]} - @Rp.{keranjang[i][3]} - "
                      f"{keranjang[i][4]}")
    else:
        print("Keranjang Anda masih kosong.")


# Variabel & Array
cpu_awal = [["CPU", "AMD_Ryzen_3-3200G", "1330000", "AM4,_DDR4"], ["CPU", "AMD_Ryzen_5-3400G", "3349000", "AM4,_DDR4"],
            ["CPU", "AMD_Ryzen_7-3700X", "5380000", "AM4,_DDR4"], ["CPU", "AMD_Ryzen_9-3900X", "8222000", "AM4,_DDR4"],
            ["CPU", "AMD_Ryzen_5-5600G", "2099000", "AM4,_DDR4"], ["CPU", "AMD_Ryzen_7-5700G", "3224000", "AM4,_DDR4"],
            ["CPU", "AMD_Ryzen_7-5700X", "3177000", "AM4,_DDR4"], ["CPU", "AMD_Ryzen_9-5900X", "6059000", "AM4,_DDR4"],
            ["CPU", "AMD_Ryzen_5-7600X", "4085000", "AM5,_DDR5"], ["CPU", "AMD_Ryzen_7-7700X", "5752000", "AM5,_DDR5"],
            ["CPU", "AMD_Ryzen_9-7900X", "7649000", "AM5,_DDR5"],
            ["CPU", "Intel_Core_i5-11400F", "1929000", "LGA1200,_DDR4"],
            ["CPU", "Intel_Core_i7-11700", "4142000", "LGA1200,_DDR4"],
            ["CPU", "Intel_Core_i9-11900F", "7597000", "LGA1200,_DDR4"],
            ["CPU", "Intel_Core_i3-12100F", "1439000", "LGA1700,_DDR4,_DDR5"],
            ["CPU", "Intel_Core_i5-12400F", "2488000", "LGA1700,_DDR4,_DDR5"],
            ["CPU", "Intel_Core_i7-12700F", "4588000", "LGA1700,_DDR4,_DDR5"],
            ["CPU", "Intel_Core_i9-12900K", "7444000", "LGA1700,_DDR4,_DDR5"],
            ["CPU", "Intel_Core_i3-13100", "2342000", "LGA1700,_DDR4,_DDR5"],
            ["CPU", "Intel_Core_i5-13400F", "3444000", "LGA1700,_DDR4,_DDR5"],
            ["CPU", "Intel_Core_i7-13700K", "6613000", "LGA1700,_DDR4,_DDR5"],
            ["CPU", "Intel_Core_i9-13900K", "9295000", "LGA1700,_DDR4,_DDR5"]]
mobo_awal = [["Motherboard", "MSI_B450-A_Pro_MAX", "1189000", "AM4,_DDR4,_PCIe_3.0,_ATX"],
             ["Motherboard", "MSI_B450_Gaming+_MAX", "1549000", "AM4,_DDR4,_PCIe_3.0,_ATX"],
             ["Motherboard", "MSI_B450M_Pro_VDH_MAX", "1255000", "AM4,_DDR4,_PCIe_3.0,_mATX"],
             ["Motherboard", "ASUS_TUF_Gaming_B450M_ProII", "1375000", "AM4,_DDR4,_PCIe_3.0,_mATX"],
             ["Motherboard", "ASRock_B450M_Steel_Legend", "1395000", "AM4,_DDR4,_PCIe_3.0,_mATX"],
             ["Motherboard", "Gigabyte_X570_UD", "2903000", "AM4,_DDR4,_PCIe_3.0,_ATX"],
             ["Motherboard", "ASUS_TUF_Gaming_X570-Plus", "3844000", "AM4,_DDR4,_PCIe_3.0,_ATX"],
             ["Motherboard", "Gigabyte_B650M_DS3H", "2993000", "AM5,_DDR5,_PCIe_3.0,_PCIe_4.0,_mATX"],
             ["Motherboard", "ASRock_B650_Pro_RS", "3775000", "AM5,_DDR5,_PCIe_3.0,_PCIe_4.0,_ATX"],
             ["Motherboard", "Gigabyte_X670_Gaming_AX", "5249000", "AM5,_DDR5,_PCIe_3.0,_PCIe_4.0,_ATX"],
             ["Motherboard", "ASUS_ROG_STRIX_X670E-F_Gaming_WiFi", "7400000", "AM5,_DDR5,_PCIe_4.0,_ATX"],
             ["Motherboard", "Gigabyte_H510M_H_Rev1.7", "1199000", "LGA1200,_DDR4,_PCIe_4.0,_mATX"],
             ["Motherboard", "ASUS_PRIME_H510M-K", "1165000", "LGA1200,_DDR4,_PCIe_3.0,_PCIe_4.0,_mATX"],
             ["Motherboard", "MSI_Z590-A_Pro", "3330000", "LGA1200,_DDR4,_PCIe_3.0,_PCIe_4.0,_ATX"],
             ["Motherboard", "MSI_Pro_B760M-P_DDR5", "3330000", "LGA1700,_DDR5,_PCIe_3.0,_PCIe_4.0,_mATX"],
             ["Motherboard", "ASRock_B760M-HDVP", "1878000", "LGA1700,_DDR5,_PCIe_3.0,_PCIe_4.0,_mATX"],
             ["Motherboard", "Gigabyte_B760M_DS3H_AX", "2697000", "LGA1700,_DDR5,_PCIe_3.0,_PCIe_4.0,_mATX"],
             ["Motherboard", "ASUS_PRIME_B760M-A_WiFi", "2988000", "LGA1700,_DDR5,_PCIe_3.0,_PCIe_4.0,_mATX"],
             ["Motherboard", "ASRock_B760M_Steel_Legend_WiFi", "3034000", "LGA1700,_DDR5,_PCIe_3.0,_PCIe_4.0,_mATX"],
             ["Motherboard", "BIOSTAR_Z790A-SILVER", "3799000", "LGA1700,_DDR5,_PCIe_3.0,_PCIe_4.0,_ATX"],
             ["Motherboard", "Gigabyte_Z790_UD_AX", "3985000", "LGA1700,_DDR5,_PCIe_3.0,_PCIe_4.0,_ATX"],
             ["Motherboard", "ASUS_ROG_STRIX_Z790-F_Gaming_WiFi", "7575000", "LGA1700,_DDR5,_PCIe_3.0,_PCIe_4.0,_ATX"]]
cpucooler_awal = [["CPU_Cooler", "Cooler_Master_Hyper_212_Spectrum_V3", "362000", "AM4,_AM5,_LGA1200,_LGA1700"],
                  ["CPU_Cooler", "Arctic_Freezer_7_X_CO", "401000", "AM4,_AM5,_LGA1200,_LGA1700"],
                  ["CPU_Cooler", "Cube_Gaming_Storm_V2", "330000", "AM4,_AM5,_LGA1200,_LGA1700"],
                  ["CPU_Cooler", "Noctua_NH-U9S_CH.BK_Chromax_Black", "1163000", "AM4,_AM5,_LGA1200,_LGA1700"],
                  ["CPU_Cooler", "Cooler_Master_MasterLiquid_240L", "1194000", "AM4,_AM5,_LGA1200,_LGA1700"],
                  ["CPU_Cooler", "NZXT_Kraken_240", "2065000", "AM4,_AM5,_LGA1200,_LGA1700"],
                  ["CPU_Cooler", "Cooler_Master_MasterLiquid_360L", "1434000", "AM4,_AM5,_LGA1200,_LGA1700"],
                  ["CPU_Cooler", "Corsair_iCUE_H150i_Elite_Capellix_XT", "2692000", "AM4,_AM5,_LGA1200,_LGA1700"]]
gpu_awal = [["VGA_Card", "GALAX_GeForce_RTX_3060_12GB", "5000000", "PCIe_4.0"],
            ["VGA_Card", "ASUS_GeForce_RTX_2060_6GB", "3997000", "PCIe_3.0"],
            ["VGA_Card", "MSI_GeForce_GTX_1650_4GB_Ventus_XS_OC", "2535000", "PCIe_3.0"],
            ["VGA_Card", "MSI_GeForce_GTX_1660_Super_6GB_Ventus_XS_OC", "3783000", "PCIe_3.0"],
            ["VGA_Card", "MSI_GeForce_RTX_3050_8GB_Ventus_2X_OC", "2535000", "PCIe_4.0"],
            ["VGA_Card", "Colorful_GeForce_GTX_1650_4GB", "2399000", "PCIe_3.0"],
            ["VGA_Card", "MSI_GeForce_RTX_4070_Ti_12GB_Ventus_3X_OC", "15490000", "PCIe_4.0"],
            ["VGA_Card", "Gigabyte_GeForce_RTX_3050_8GB_Eagle_OC", "4408000", "PCIe_4.0"],
            ["VGA_Card", "Zotac_GeForce_RTX_4060_Ti_48B_Twin_Edge", "6675000", "PCIe_4.0"],
            ["VGA_Card", "Gigabyte_GeForce_RTX_4090_24GB_Gaming_OC", "30367000", "PCIe_4.0"],
            ["VGA_Card", "ASRock_Radeon_RX_6600_8GB_Challenger_D", "3412000", "PCIe_4.0"],
            ["VGA_Card", "PowerColor_Radeon_RX_550_4GB_Red_Dragon", "1711000", "PCIe_3.0"],
            ["VGA_Card", "ASRock_Radeon_RX_6500_XT_4GB_Phantom_Gaming_D", "2488000", "PCIe_4.0"],
            ["VGA_Card", "Arktek_Radeon_RX_580_8GB_Cyclops", "1781000", "PCIe_3.0"],
            ["VGA_Card", "MSI_Radeon_RX_6400_4GB_Aero_ITX", "2259000", "PCIe_4.0"],
            ["VGA_Card", "PowerColor_Radeon_RX_7900_XTX_24GB_Red_Devil", "21362000", "PCIe_4.0"]]
ram_awal = [["RAM", "KLEVV_BOLT_X_Series_2x8GB_3200MHz", "682000", "DDR4"],
            ["RAM", "Team_Elite_Plus_Black_2x4GB_2400MHz", "500000", "DDR4"],
            ["RAM", "Corsair_Vengeance_LPX_2x8GB_2666MHz", "777000", "DDR4"],
            ["RAM", "ADATA_XPG_SPECTRIX_2x8GB_3200MHz", "885000", "DDR4"],
            ["RAM", "V-GeN_Tsunami_2x4GB_3200MHz", "581000", "DDR4"],
            ["RAM", "G.Skill_TridentZ_2x8GB_3600MHz", "980000", "DDR4"],
            ["RAM", "Team_Elite_Plus_Black_2x16GB_5200MHz", "1617000", "DDR5"],
            ["RAM", "Corsair_Vengeance_2x16GB_6400MHz", "2373000", "DDR5"],
            ["RAM", "Team_Delta_RGB_2x16GB_6400MHz", "2833000", "DDR5"],
            ["RAM", "ADATA_XPG_Lancer_2x16GB_7200MHz", "3075000", "DDR5"]]
psu_awal = [["PSU", "1STPLAYER_PS-500AX_500W_80+_Bronze", "595000", "-"],
            ["PSU", "Cooler_Master_MWE_500_500W_80+_Bronze", "771000", "-"],
            ["PSU", "Corsair_CV_Series_650W_80+_Bronze", "1032000", "-"],
            ["PSU", "Seasonic_Focus_Gold_GX-550_550W_80+_Gold", "1527000", "-"],
            ["PSU", "Super_Flower_Leadex_III_750W_80+_Gold", "1761000", "-"],
            ["PSU", "FSP_Hydro_G_Pro_750W_80+_Gold", "1836000", "-"],
            ["PSU", "Corsair_HX_Series_1000W_80+_Platinum", "3501000", "-"],
            ["PSU", "Seasonic_Prime_TX-650_650W_80+_Titanium", "295000", "-"],
            ["PSU", "BeQuiet!_Pure_Power_10_600W_80+_Silver", "1140000", "-"],
            ["PSU", "Super_Flower_Leadex_1600W_80+_Platinum", "4650000", "-"]]
storage_awal = [["HDD", "WDC_Caviar_Blue_1TB_SATA3", "636000", "-"], ["HDD", "Seagate_2TB_SATA3", "896000", "-"],
                ["HDD", "WDC_Blue_2TB_SATA3", "912000", "-"], ["HDD", "Seagate_4TB_SATA3", "1507000", "-"],
                ["SSD", "ADATA_SU650_240GB_SATA3", "219000", "-"],
                ["SSD", "Samsung_870_EVO_500GB_SATA3", "724000", "-"],
                ["SSD", "V-GeN_256GB_SATA3", "279000", "-"], ["SSD", "ADATA_SU800_512GB_SATA3", "891000", "-"],
                ["SSD", "ADATA_SX6000_Lite_256GB_NVMe", "290000", "PCIe_3.0"],
                ["SSD", "Samsung_970_EVO_500GB_NVMe", "585000", "PCIe_3.0"],
                ["SSD", "Samsung_980_PRO_500GB_NVMe", "1001000", "PCIe_4.0"],
                ["SSD", "Samsung_990_PRO_1TB_NVMe", "1700000", "PCIe_4.0"]]
case_awal = [["Case", "Cube_GAMING_BLIG", "366000", "mATX,_ATX"], ["Case", "Cube_GAMING_BYRON", "381000", "mATX,_ATX"],
             ["Case", "Cube_GAMING_LICHT", "478000", "mATX,_ATX"],
             ["Case", "Cube_GAMING_DUSTIN_WHITE", "564000", "mATX,_ATX"],
             ["Case", "Cube_GAMING_XAURES_WHITE", "595000", "mATX,_ATX"],
             ["Case", "Cube_GAMING_SLEV_WHITE", "773000", "mATX,_ATX"],
             ["Case", "LIAN_LI_LANCOOL_205_Black", "977000", "mATX,_ATX"],
             ["Case", "Paradox_Gaming_Durandal_Black", "505000", "mATX"],
             ["Case", "Aigo_DarkFlash_DLM21", "594000", "mATX"], ["Case", "MSI_MAG_Forge_M100A", "667000", "mATX"],
             ["Case", "MSI_MAG_Vampiric_100R", "855000", "mATX,_ATX"],
             ["Case", "NZXT_H7_Flow_Black", "1836000", "mATX,_ATX"]]
fan_awal = [["Fan", "Cube_Gaming_Fix_Rainbow_12cm", "47000", "-"], ["Fan", "PCCooler_FX-120", "54000", "-"],
            ["Fan", "Aigo_DarkFlash_CL12_12cm", "59000", "-"], ["Fan", "Deepcool_RF_120FS_12cm", "74000", "-"],
            ["Fan", "Noctua_Premium_Fan_12cm", "364000", "-"], ["Fan", "Enermax_SquA_RGB_12cm", "205000", "-"],
            ["Fan", "Arctic_F12_PWN_PST_12cm", "135000", "-"], ["Fan", "Aerocool_Mirage_12_ARGB_12cm", "146000", "-"]]
file_produk = ['cpu.txt', 'motherboard.txt', 'cpucooler.txt', 'gpu.txt', 'ram.txt', 'psu.txt', 'storage.txt',
               'case.txt', 'fan.txt']
produk_awal = [cpu_awal, mobo_awal, cpucooler_awal, gpu_awal, ram_awal, psu_awal, storage_awal, case_awal, fan_awal]
produk = []
keranjang = []
jumlah = []
nama_komponen = ['CPU', "Motherboard", "CPU Cooler", "VGA Card", "RAM", "PSU", "Storage", "Case", "Fan"]

# Perintah 1x pakai
nama = login()
cek_produk()

# Peritah selama program berjalan
while True:
    if nama == "1":
        print("\n=== Menu Admin ===")
        print("1. Tampilkan Daftar Produk")
        print("2. Tambah Produk")
        print("3. Hapus Produk")
        print("4. Urutkan Produk")
        print("5. Cari Produk")
        print("6. Kembali")
        pilihan_menu = input("Masukkan Pilihan: ")

        if pilihan_menu == "0":
            print("\n=== Menu Admin ===")
            print("1. Tampilkan Daftar Produk")
            print("2. Tambah Produk")
            print("3. Hapus Produk")
            print("4. Urutkan Produk")
            print("5. Cari Produk")
            print("6. Kembali")
            pilihan_menu = input("Masukkan Pilihan: ")
        elif pilihan_menu == "1":
            clear()
            print(
                "=== Pilih komponen yang akan ditampilkan ==="
                "\n1. CPU"
                "\n2. Motherboard"
                "\n3. CPU Cooler"
                "\n4. VGA Card"
                "\n5. RAM"
                "\n6. PSU"
                "\n7. Storage"
                "\n8. Case"
                "\n9. Fan"
                "\n0. Kembali"
            )
            try:
                pilihan_komponen = int(input("Masukkan Pilihan: "))
            except ValueError:
                print("Pilihan tidak valid.")
                continue
            else:
                if 1 <= pilihan_komponen <= 9:
                    clear()
                    tampilkan_daftar_produk(pilihan_komponen)
                else:
                    clear()
                    pilihan_menu = "0"
        elif pilihan_menu == "2":
            clear()
            print(
                "=== Pilih komponen yang akan ditambahkan ==="
                "\n1. CPU"
                "\n2. Motherboard"
                "\n3. CPU Cooler"
                "\n4. VGA Card"
                "\n5. RAM"
                "\n6. PSU"
                "\n7. Storage"
                "\n8. Case"
                "\n9. Fan"
                "\n0. Kembali"
            )
            try:
                input_komponen = int(input("Masukkan Pilihan: "))
            except ValueError:
                print("Pilihan tidak valid.")
                continue
            else:
                if 1 <= input_komponen <= 9:
                    input_namap = input("Masukkan Nama Produk: ")
                    input_harga = input("Masukkan Harga: ")
                    input_spek = input("Masukkan Spesifikasi Kunci: ")
                    produk_baru = [nama_komponen[input_komponen - 1], input_namap, input_harga, input_spek]
                    tambah_produk(input_komponen, produk_baru)
                    clear()
                    print("Produk berhasil ditambahkan.")
                else:
                    clear()
                    pilihan_menu = "0"
        elif pilihan_menu == "3":
            clear()
            print(
                "=== Pilih komponen yang akan dihapus ==="
                "\n1. CPU"
                "\n2. Motherboard"
                "\n3. CPU Cooler"
                "\n4. VGA Card"
                "\n5. RAM"
                "\n6. PSU"
                "\n7. Storage"
                "\n8. Case"
                "\n9. Fan"
                "\n0. Kembali"
            )
            try:
                input_komponen = int(input("Masukkan Pilihan: "))
            except ValueError:
                print("Pilihan tidak valid.")
                continue
            else:
                if 1 <= input_komponen <= 9:
                    clear()
                    tampilkan_daftar_produk(input_komponen)
                    try:
                        input_hapus = int(input("Masukkan Nomor Produk: "))
                    except ValueError:
                        print("Pilihan tidak valid.")
                        continue
                    else:
                        if 1 <= input_hapus <= 9:
                            hapus_produk(input_komponen, input_hapus)
                            clear()
                            print("Produk berhasil dihapus.")
                        else:
                            clear()
                            pilihan_menu = "0"
                else:
                    clear()
                    pilihan_menu = "0"
        elif pilihan_menu == "4":
            clear()
            print(
                "=== Pilih komponen yang akan diurutkan ==="
                "\n1. CPU"
                "\n2. Motherboard"
                "\n3. CPU Cooler"
                "\n4. VGA Card"
                "\n5. RAM"
                "\n6. PSU"
                "\n7. Storage"
                "\n8. Case"
                "\n9. Fan"
                "\n0. Kembali"
            )
            try:
                input_komponen = int(input("Masukkan pilihan: "))
            except ValueError:
                print("Pilihan tidak valid.")
                continue
            else:
                if 1 <= input_komponen <= 9:
                    clear()
                    print("Urutkan berdasarkan:"
                          "\n1. Nama produk (A-Z)"
                          "\n2. Nama produk (Z-A)"
                          "\n3. Harga terendah"
                          "\n4. Harga tertinggi"
                          "\n5. Spek kunci (A-Z)"
                          "\n6. Spek kunci (Z-A)"
                          "\n0. Kembali")
                    input_urutan = "-1"
                    while input_urutan != "0" or input_urutan != "1" or input_urutan != "2" or input_urutan != "3"\
                            or input_urutan != "4" or input_urutan != "5" or input_urutan != "6":
                        input_urutan = input("Masukan pilihan: ")
                        if input_urutan == "0" or input_urutan == "1" or input_urutan == "2" or input_urutan == "3"\
                                or input_urutan == "4" or input_urutan == "5" or input_urutan == "6":
                            break
                    if input_urutan == "1":
                        urutkan_produk(input_komponen, 1, False)
                    elif input_urutan == "2":
                        urutkan_produk(input_komponen, 1, True)
                    elif input_urutan == "3":
                        urutkan_produk(input_komponen, 2, False)
                    elif input_urutan == "4":
                        urutkan_produk(input_komponen, 2, True)
                    elif input_urutan == "5":
                        urutkan_produk(input_komponen, 3, False)
                    elif input_urutan == "6":
                        urutkan_produk(input_komponen, 3, True)
                    else:
                        input_komponen = 0
                    clear()
                    if input_urutan != "0" or input_urutan != "1" or input_urutan != "2" or input_urutan != "3" \
                            or input_urutan != "4" or input_urutan != "5" or input_urutan != "6":
                        print("Produk berhasil diurutkan.")
                else:
                    clear()
                    pilihan_menu = "0"
        elif pilihan_menu == "5":
            cari_kata = input("Masukkan kata kunci: ")
            ketemu = cari_produk(cari_kata)
            if ketemu == -1:
                print("Maaf, produk dengan kata kunci yang Anda cari tidak ada.")
            else:
                clear()
                print(f"Produk dengan kata kunci {cari_kata}:")
                tampilkan_daftar_produk(ketemu, True)
        elif pilihan_menu == "6":
            clear()
            nama = login()
    elif nama == "keluar":
        break
    else:
        print("\n=== Menu Pembeli ==="
              "\n1. Tampilkan Daftar Produk"
              "\n2. Tampilkan Keranjang"
              "\n3. Masukkan Keranjang"
              "\n4. Hapus Keranjang"
              "\n5. Urutkan Produk"
              "\n6. Cari Produk"
              "\n7. Checkout"
              "\n8. Kembali")
        pilihan_menu = input("Masukkan Pilihan: ")

        if pilihan_menu == "0":
            print("\n=== Menu Pembeli ==="
                  "\n1. Tampilkan Daftar Produk"
                  "\n2. Tampilkan Keranjang"
                  "\n3. Masukkan Keranjang"
                  "\n4. Hapus Keranjang"
                  "\n5. Urutkan Produk"
                  "\n6. Cari Produk"
                  "\n7. Checkout"
                  "\n8. Kembali")
            pilihan_menu = input("Masukkan Pilihan: ")
        elif pilihan_menu == "1":
            clear()
            print(
                "=== Pilih komponen yang akan ditampilkan ==="
                "\n1. CPU"
                "\n2. Motherboard"
                "\n3. CPU Cooler"
                "\n4. VGA Card"
                "\n5. RAM"
                "\n6. PSU"
                "\n7. Storage"
                "\n8. Case"
                "\n9. Fan"
                "\n0. Kembali"
            )
            try:
                pilihan_komponen = int(input("Masukkan Pilihan: "))
            except ValueError:
                print("Pilihan tidak valid.")
                continue
            else:
                if 1 <= pilihan_komponen <= 9:
                    clear()
                    tampilkan_daftar_produk(pilihan_komponen)
                else:
                    clear()
                    pilihan_menu = "0"
        elif pilihan_menu == "2":
            clear()
            print("Produk-produk di dalam keranjang:")
            tampilkan_keranjang()
        elif pilihan_menu == "3":
            clear()
            print(
                "=== Pilih komponen yang akan dibeli ==="
                "\n1. CPU"
                "\n2. Motherboard"
                "\n3. CPU Cooler"
                "\n4. VGA Card"
                "\n5. RAM"
                "\n6. PSU"
                "\n7. Storage"
                "\n8. Case"
                "\n9. Fan"
                "\n0. Kembali"
            )
            try:
                pilihan_komponen = int(input("Masukkan Pilihan: "))
            except ValueError:
                print("Pilihan tidak valid.")
                continue
            else:
                if 1 <= pilihan_komponen <= 9:
                    clear()
                    tampilkan_daftar_produk(pilihan_komponen)
                    try:
                        pilihan_produk = int(input("Masukkan Pilihan: "))
                    except ValueError:
                        print("Pilihan tidak valid.")
                        continue
                    else:
                        if 1 <= pilihan_produk <= len(produk[pilihan_komponen - 1]):
                            try:
                                jumlah_beli = int(input("Masukkan Jumlah: "))
                            except ValueError:
                                print("Jumlah tidak valid.")
                                continue
                            else:
                                masuk_keranjang = produk[pilihan_komponen - 1][pilihan_produk - 1][:]
                                masuk_keranjang.insert(0, jumlah_beli)
                                keranjang.append(masuk_keranjang)
                                clear()
                                print("Produk berhasil ditambahkan ke keranjang.")
                                pilihan_menu = "0"
                        else:
                            clear()
                            pilihan_menu = "0"
                else:
                    clear()
                    pilihan_menu = "0"
        elif pilihan_menu == "4":
            clear()
            if len(keranjang) > 0:
                print("Pilih produk yang akan dihapus dari keranjang:")
            tampilkan_keranjang()
            if len(keranjang) > 0:
                try:
                    pilihan_nomor = int(input("Masukkan Nomor: "))
                except ValueError:
                    print("Pilihan tidak valid.")
                    continue
                else:
                    if 1 <= pilihan_nomor <= len(keranjang):
                        keranjang.pop(pilihan_nomor-1)
                        print("Produk berhasil dihapus dari keranjang.")
                        clear()
                    else:
                        clear()
                        pilihan_menu = "0"
        elif pilihan_menu == "5":
            clear()
            print(
                "=== Pilih komponen yang akan diurutkan ==="
                "\n1. CPU"
                "\n2. Motherboard"
                "\n3. CPU Cooler"
                "\n4. VGA Card"
                "\n5. RAM"
                "\n6. PSU"
                "\n7. Storage"
                "\n8. Case"
                "\n9. Fan"
                "\n0. Kembali"
            )
            try:
                input_komponen = int(input("Masukkan pilihan: "))
            except ValueError:
                print("Pilihan tidak valid.")
                continue
            else:
                if 1 <= input_komponen <= 9:
                    clear()
                    print("Urutkan berdasarkan:"
                          "\n1. Nama produk (A-Z)"
                          "\n2. Nama produk (Z-A)"
                          "\n3. Harga terendah"
                          "\n4. Harga tertinggi"
                          "\n5. Spek kunci (A-Z)"
                          "\n6. Spek kunci (Z-A)"
                          "\n0. Kembali")
                    input_urutan = "-1"
                    while input_urutan != "0" or input_urutan != "1" or input_urutan != "2" or input_urutan != "3" \
                            or input_urutan != "4" or input_urutan != "5" or input_urutan != "6":
                        input_urutan = input("Masukan pilihan: ")
                        if input_urutan == "0" or input_urutan == "1" or input_urutan == "2" or input_urutan == "3" \
                                or input_urutan == "4" or input_urutan == "5" or input_urutan == "6":
                            break
                    if input_urutan == "1":
                        urutkan_produk(input_komponen, 1, False, False)
                    elif input_urutan == "2":
                        urutkan_produk(input_komponen, 1, True, False)
                    elif input_urutan == "3":
                        urutkan_produk(input_komponen, 2, False, False)
                    elif input_urutan == "4":
                        urutkan_produk(input_komponen, 2, True, False)
                    elif input_urutan == "5":
                        urutkan_produk(input_komponen, 3, False, False)
                    elif input_urutan == "6":
                        urutkan_produk(input_komponen, 3, True, False)
                    else:
                        input_komponen = 0
                    clear()
                    if input_urutan != "0" or input_urutan != "1" or input_urutan != "2" or input_urutan != "3" \
                            or input_urutan != "4" or input_urutan != "5" or input_urutan != "6":
                        print("Produk berhasil diurutkan.")
                else:
                    clear()
                    pilihan_menu = "0"
        elif pilihan_menu == "6":
            cari_kata = input("Masukkan kata kunci: ")
            ketemu = cari_produk(cari_kata)
            if ketemu == -1:
                print("Maaf, produk dengan kata kunci yang Anda cari tidak ada.")
            else:
                clear()
                print(f"Produk dengan kata kunci {cari_kata}:")
                tampilkan_daftar_produk(ketemu, True)
        elif pilihan_menu == "7":
            clear()
            print("Produk-produk yang akan dibeli:")
            tampilkan_keranjang()
            harga = harga_keranjang()
            if harga > 0:
                print(f"Total pembelian = Rp.{harga}"
                      f"\n\nApakah pembelian Anda sudah benar?"
                      f"\n1. Ya"
                      f"\n2. Belum")
                try:
                    konfirmasi = int(input("Masukkan pilihan: "))
                except ValueError:
                    print("Pilihan tidak valid.")
                    continue
                else:
                    if konfirmasi == 1:
                        print("\nApakah Anda ingin menggunakan jasa perakitan kami?"
                              "\nBiaya dari jasa ini adalah sebesar Rp.100,000."
                              "\n1. Ya"
                              "\n2. Tidak")
                        try:
                            perakitan = int(input("Masukkan pilihan: "))
                        except ValueError:
                            print("Pilihan tidak valid.")
                            continue
                        else:
                            if 1 <= perakitan <= 2:
                                if perakitan == 1:
                                    harga += 100000
                                for i in range(len(keranjang)):
                                    keranjang[i][0] = str(keranjang[i][0])
                                    keranjang[i][3] = f"@Rp.{int(keranjang[i][3]):,}"
                                keranjang.append(["Harga total pembelian = Rp." + f"{int(harga):,}"])
                                if perakitan == 1:
                                    keranjang.append(["Pakai jasa perakitan"])
                                file_pembelian()
                                keranjang = []
                            else:
                                clear()
                                pilihan_menu = "0"
                    else:
                        clear()
                        pilihan_menu = "0"
        elif pilihan_menu == "8":
            keranjang = []
            clear()
            nama = login()
