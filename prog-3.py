spare_parts = ['CPU', 'Motherboard', 'CPU Cooler', 'VGA', 'RAM', 'PSU', 'Storage', 'Casing', 'Fan']
def checkout(cart):
    total = 0
    for item in cart:
        if item in spare_parts:
            total += get_price(item)
        else:
            print(f"{item} is not a valid spare part.")
    print(f"Total: {total}")
def get_price(item):
    prices = {
        'CPU': 300,
        'Motherboard': 150,
        'CPU Cooler': 50,
        'VGA': 200,
        'RAM': 100,
        'PSU': 100,
        'Storage': 80,
        'Casing': 70,
        'Fan': 20
    }
    return prices[item]

#atau

produk = {
    'CPU': {'nama': 'Intel Core i7', 'harga': 4000000},
    'Motherboard': {'nama': 'ASUS ROG', 'harga': 2000000},
    'Cpu Cooler': {'nama': 'Cooler Master', 'harga': 500000},
    # ...
}
keranjang = []
while True:
    print('Produk yang tersedia:')
    for kategori, data in produk.items():
        print(f'{kategori}: {data['nama']} - Rp{data['harga']}')
    pilihan = input('Masukkan kategori produk yang ingin Anda beli (ketik "selesai" untuk selesai): ')
    if pilihan == 'selesai':
        break
    elif pilihan in produk:
        keranjang.append(produk[pilihan])
        print(f'{produk[pilihan]['nama']} telah ditambahkan ke keranjang')
    else:
        print('Pilihan tidak valid')

    total = 0
    print('Ringkasan pesanan:')
    for item in keranjang:
        print(f"{item['nama']} - Rp{item['harga']}")
    total += item['harga']
    print(f'Total: Rp{total}')

    alamat = input('Masukkan alamat pengiriman: ')
    metode_pengiriman = input('Masukkan metode pengiriman (JNE/TIKI/POS): ')

    metode_pembayaran = input('Masukkan metode pembayaran (transfer/kartu kredit/COD): ')
    if metode_pembayaran == 'transfer':
    # Proses pembayaran via transfer
        elif
    metode_pembayaran == 'kartu kredit':
    # Proses pembayaran via kartu kredit
    elif metode_pembayaran == 'COD':
    # Proses pembayaran via COD
    else:
    print('Metode pembayaran tidak valid')


