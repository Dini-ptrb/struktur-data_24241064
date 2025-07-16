# Meminta pengguna memasukkan nama costumer 
jumlah_costumer = int(input("Masukkan jumlah costumer: "))

# Dictionary untuk menyimpan data
data_costumer = {}

# Perulangan untuk input data setiap costumer
for i in range(jumlah_costumer):
    print(f"\ncostumer ke-{i+1}")
    nama_costumer = input("Masukkan nama_costumer: ")         # str
    tanggal_belanja = input("Masukkan tanggal_belanja: ")       # str
    jumlah_barang = input("masukkan jumlah_barang: ")    # str
    
    # List untuk menyimpan tuple (nama barang, harga)
    jumlah_beli = []

    nama_barang = int(input("Masukkan jumlah barang: "))  # int
    for j in range(nama_barang):
        nama_barang  = input(f"  Nama barang ke-{j+1}: ")         # str
        harga = float(input(f"  harga untuk {nama_barang}: "))        # float
        jumlah_beli.append((nama_barang,harga))                     # tuple dalam list