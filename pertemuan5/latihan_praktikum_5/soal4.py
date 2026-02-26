# 4. Diberikan data buku dalam bentuk dictionary:
transaksi = [
{"produk": "Buku", "harga": 10000, "jumlah": 3},
{"produk": "Pena", "harga": 5000, "jumlah": 10},
{"produk": "Penghapus", "harga": 2000, "jumlah": 2}
]
# a. Ubah jumlah buku menjadi 8.
transaksi [0]["jumlah"] = 8
print(transaksi)
print(transaksi)
print()
# b. Tambahkan 2 produk baru.
transaksi.append({"produk" : "balilil", "harga" : 3000, "jumlah" : 6})
transaksi.append({"produk" : "maswowo", "harga" : 3100, "jumlah" : 3})
print(transaksi)
print()
# c. Hitung Total Pendapatan (Harga x Jumlah) untuk setiap transaksi menggunakan
# perulangan.
indeks=0
for x in transaksi:
    print(f"produk:{transaksi[indeks]["produk"]} | Total:  {transaksi[indeks]["harga"]*transaksi[indeks]["jumlah"]}")
    indeks += 1
