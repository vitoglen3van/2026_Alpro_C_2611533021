print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")
nama_3021 = input("Masukkan Nama Pengunjung        : ")
umur_3021 = int(input("Input umur anda                 : "))

# .strip().lower() untuk menangani input string
sim_3021 = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()

# Menu Paket Wahana
print("\nPilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")

paket_3021 = input("Masukkan nomor paket (1-5)      : ").strip()
jumlah_tiket_3021 = int(input("Masukkan jumlah tiket           : "))

# Pilar 1: IF Tunggal untuk Validasi Kelogisan Tiket
if jumlah_tiket_3021 <= 0:
    print("[PERINGATAN] Kuota tiket tidak valid!")
    exit()

is_member_3021 = input("Apakah Anda member? (y/t)       : ").strip().lower()
kode_promo_valid_3021 = input("Apakah kode promo valid? (y/t)  : ").strip().lower()

# Inisialisasi variabel pendukung
harga_satuan_3021 = 0
status_akses_3021 = ""

# Pilar 2: MATCH - CASE untuk Pemilihan Wahana
match paket_3021:
    case "1":
        harga_satuan_3021 = 50000
    case "2":
        harga_satuan_3021 = 75000
    case "3":
        harga_satuan_3021 = 120000
    case "4":
        harga_satuan_3021 = 100000
    case "5":
        harga_satuan_3021 = 220000
    case _:
        print("Paket wahana tidak valid!")
        exit()

# Pilar 3: IF - ELIF - ELSE dan Operator Logika untuk Validasi Izin Kendali
print("\n--- KELAYAKAN PENGENDARA WAHANA ---")
if paket_3021 == "3":
    if umur_3021 >= 17 and sim_3021 == 'y':
        status_akses_3021 = "Anda sudah dewasa dan boleh mengendarai ATV sendiri."
    elif umur_3021 >= 17 and sim_3021 != 'y':
        status_akses_3021 = "Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur)."
    elif umur_3021 < 17 and sim_3021 == 'y':
        status_akses_3021 = "Identitas tidak valid: Belum cukup umur memiliki SIM."
    else:
        status_akses_3021 = "Anda belum cukup umur dan tidak boleh bawa motor ATV."
else:
    if umur_3021 >= 10:
        status_akses_3021 = "Anda memenuhi syarat umur untuk menikmati wahana ini."
    else:
        status_akses_3021 = "Anda belum cukup umur untuk menikmati wahana ini."

print(f"Status Akses: {status_akses_3021}")

# Perhitungan Subtotal
subtotal_3021 = harga_satuan_3021 * jumlah_tiket_3021
total_diskon_persen_3021 = 0

# Pilar 4: MULTI-IF Terpisah untuk Akumulasi Diskon Bertingkat
if subtotal_3021 >= 200000:
    total_diskon_persen_3021 += 10

if is_member_3021 in ['y', 'ya']:
    total_diskon_persen_3021 += 5

if kode_promo_valid_3021 in ['y', 'ya']:
    total_diskon_persen_3021 += 15

if jumlah_tiket_3021 >= 5:
    total_diskon_persen_3021 += 5

# Perhitungan Nominal Diskon dan Total Bayar
nominal_diskon_3021 = subtotal_3021 * (total_diskon_persen_3021 / 100)
total_bayar_3021 = subtotal_3021 - nominal_diskon_3021

# Pilar 5: IF - ELSE untuk Evaluasi Kelulusan Audit & Bonus
catatan_layanan_3021 = ""
if total_bayar_3021 > 300000:
    catatan_layanan_3021 = "Selamat! Anda berhak mendapatkan Souvenir Gratis."
else:
    catatan_layanan_3021 = "Terima kasih telah berkunjung."

# OUTPUT RINCIAN PEMBAYARAN (Format Desimal f-string)
print("\n--- Rincian Pembayaran ---")
print(f"Subtotal Belanja : Rp {subtotal_3021:,.0f}")
print(f"Total Diskon     : {total_diskon_persen_3021}% (Rp {nominal_diskon_3021:,.0f})")
print(f"Total Bayar      : Rp {total_bayar_3021:,.0f}")
print(f"Catatan Layanan  : {catatan_layanan_3021}")
print("Program Selesai")