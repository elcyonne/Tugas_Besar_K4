#workspacefikri
# Data produk komputer
produk = [
    {'nama': 'Laptop ASUS', 'deskripsi': 'Laptop ASUS dengan spesifikasi tinggi', 'merek': 'ASUS', 'harga': 10000000},
    {'nama': 'Mouse Logitech', 'deskripsi': 'Mouse gaming Logitech dengan DPI tinggi', 'merek': 'Logitech', 'harga': 500000},
    {'nama': 'Monitor Dell', 'deskripsi': 'Monitor Dell dengan resolusi 4K', 'merek': 'Dell', 'harga': 3000000}
]

# Fungsi pencarian produk
def search_produk(keyword):
    results = []
    for item in produk:
        if keyword.lower() in item['nama'].lower() or keyword.lower() in item['deskripsi'].lower() or keyword.lower() in item['merek'].lower():
            results.append(item['nama'])
    return results

# Input kata kunci pencarian
keyword = input("Masukkan nama produk : ")

# Melakukan pencarian produk
search_results = search_produk(keyword)

# Menampilkan hasil pencarian
if len(search_results) == 0:
    print("Tidak ditemukan hasil pencarian.")
else:
    print("Hasil pencarian:")
    for result in search_results:
        print(result)