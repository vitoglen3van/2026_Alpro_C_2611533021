print("=== SISTEM TRANSAKSI TOKO ===")
nama_3021 = input("Masukkan Nama Pelanggan : ")
status_3021 = input("Masukkan Status Pelanggan (member/nonmember) : ")
total_3021 = int(input("Masukkan Total Belanja : "))
jumlah_3021 = int(input("Masukkan Jumlah Barang : "))
promo_3021 = input("Masukkan Kode Promo : ")

print("\n=== DATA TRANSAKSI ===")
print(f"Nama Pelanggan       : {nama_3021}")
print(f"Status Pelanggan     : {status_3021}")
print(f"Total Belanja        : Rp{total_3021}")
print(f"Jumlah Barang        : {jumlah_3021}")
print(f"Kode Promo           : {promo_3021}")

kode_promo_3021 = ["HEMAT10", "HIDUPMAHASISWA", "HIDUPFTI"] #list kode promo

syarat_total_3021 = total_3021 >= 200000 # apakah memenuhi syarat belanja
syarat_jumlah_3021 = jumlah_3021 >= 3 # apakah memenuhi syarat barang
status_valid_3021 = status_3021 == "member" # apakah user member
promo_valid_3021 = promo_3021 in kode_promo_3021 # apakah kode promo ada dalam list

print("\n=== HASIL VALIDASI ===")
print(f"Belanja >= Rp200000        : {syarat_total_3021}")
print(f"Jumlah Barang >= 3         : {syarat_jumlah_3021}")
print(f"Status Member              : {status_valid_3021}")
print(f"Kode Promo Tersedia        : {promo_valid_3021}")
print(f"Mendapatkan Diskon         : {syarat_jumlah_3021 or syarat_total_3021}")
print(f"Mendapatkan Promo          : {promo_valid_3021}")

diskon_3021 = 0.05

print("\n=== HASIL PERHITUNGAN ===")
print(f"Diskon                      : Rp{diskon_3021 * total_3021}")
print(f"Total Pembayaran            : Rp{total_3021 - total_3021 * diskon_3021}")
print(f"Rata-rata Harga Barang      : Rp{(total_3021 - total_3021 * diskon_3021)/jumlah_3021}")

print("\n=== HAK AKSES PELANGGAN ===")
print(f"Kode Hak Akses              : ...")
print(f"Member Access               : {status_valid_3021}")
print(f"Promo Access                : {promo_valid_3021}")
print(f"Free Shipping Access        : ...")

kode_transaksi_3021 = int(status_valid_3021) << 0 | int(syarat_total_3021) << 1 | int(syarat_jumlah_3021) << 2 | int(promo_valid_3021) << 3
kode_referensi_3021 = int(status_valid_3021) << 0 | int(syarat_total_3021) << 1 | int(promo_valid_3021) << 3

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print(f"{format(int(status_valid_3021) << 0,"04b")} | {format(int(syarat_total_3021) << 1,"04b")} | {format(int(syarat_jumlah_3021) << 2,"04b")} | {format(int(promo_valid_3021) << 3,"04b")}")
print(f"Kode Biner   : {format(kode_transaksi_3021,"04b")}")
print(f"Kode Desimal : {kode_transaksi_3021}")

print("\n=== Pemeriksaan Status ===")
print("Cek Member")
print(f"{format(kode_transaksi_3021,"04b")} & {format(int(status_valid_3021) << 0,"04b")}")
print(f"Hasil Biner   : {format((kode_transaksi_3021) & int(status_valid_3021) << 0,"04b")}")
print(f"Hasil Desimal : {(kode_transaksi_3021) & int(status_valid_3021) << 0}")

print("Cek Promo")
print(f"{format(kode_transaksi_3021,"04b")} & {format(int(promo_valid_3021) << 3,"04b")}")
print(f"Hasil Biner   : {format((kode_transaksi_3021) & int(promo_valid_3021) << 3,"04b")}")
print(f"Hasil Desimal : {(kode_transaksi_3021) & int(promo_valid_3021) << 3}")

print("\n=== Perbandingan Status ===")
print(f"Kode Transaksi : {format(kode_transaksi_3021,"04b")}")
print(f"Kode Referensi : {format(kode_referensi_3021,"04b")}")
print(f"{format(kode_transaksi_3021,"04b")} ^ {format(kode_referensi_3021,"04b")}")
print(f"Hasil Biner   : {format((kode_transaksi_3021) ^ (kode_referensi_3021),"04b")}")
print(f"Hasil Desimal : {(kode_transaksi_3021) ^ (kode_referensi_3021)}")

print("\n=== Shift ===")
print(f"{format(kode_transaksi_3021,"04b")} << 1")
print(f"Hasil Biner   : {format((kode_transaksi_3021) << 1,"04b")}")
print(f"Hasil Desimal : {(kode_transaksi_3021) << 1}") 
print("=== SELESAI ===")