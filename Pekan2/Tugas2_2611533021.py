print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")
nama_3021 = input("Masukkan Nama Mahasiswa : ")
kelamin_3021 = input("Masukkan Jenis Kelamin (L/P): ")
umur_3021 = int(input("Masukkan Umur : "))
skor_3021 = float(input("Masukkan Skor Tes Awal : "))

alamat_3021 = """
Pasar Baru,
Kecamatan Pauh,
Kota Padang,
Sumatera Barat,
Indonesia
"""
from typing import Final
kkm_3021: Final = 75.0
token_3021 = 100+3j
lulus_3021 = skor_3021 > kkm_3021

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa : ",nama_3021," | ",type(nama_3021))
print("Jenis Kelamin : ",kelamin_3021," | ",type(kelamin_3021))
print("Alamat Domisili : ",alamat_3021," | ",type(alamat_3021))
print("Umur : ",umur_3021," tahun | ",type(umur_3021))
print("Skor Tes Awal : ",skor_3021," | ",type(skor_3021))
print("ID Token Sinyal: ",token_3021," | ",type(token_3021))

print("=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai: ",kkm_3021," | ",type(kkm_3021))
print("Apakah Dinyatakan Lulus?: ",lulus_3021," | ",type(lulus_3021))