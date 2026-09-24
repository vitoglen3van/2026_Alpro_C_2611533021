#input dari user
total_belanja_3021 = float(input("Masukkan total belanja (Rp): "))

#input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_3021 = input("Apakah anda member? (y/t): ").strip().lower()
is_member_3021 = input_member_3021 in ["y", "ya"]

#input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_3021 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_3021 = input_promo_3021 in ["y", "ya"]

total_diskon_persen_3021 = 0

if total_belanja_3021 > 1000000:
    total_diskon_persen_3021 += 10 #Diskon belanja besar

if is_member_3021:
    total_diskon_persen_3021 += 5 #Diskon member

if kode_promo_valid_3021:
    total_diskon_persen_3021 += 15 #Diskon voucher

nominal_diskon_3021 = total_belanja_3021 * (total_diskon_persen_3021 / 100)
total_bayar_3021 = total_belanja_3021 - nominal_diskon_3021

print("\n--- Rincian Pembayaran ---")
print(f"Total diskon    : {total_diskon_persen_3021}% (Rp {nominal_diskon_3021:,.0f})")
print(f"Total bayar     : Rp {total_bayar_3021:,.0f}")

print(f"Total diskon yang anda dapatkan: {total_diskon_persen_3021}%")