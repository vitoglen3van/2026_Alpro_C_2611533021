# Name: Vito Glenevan
# NIM: 2611533021

full_name = "Siti Aisyah"
nim = "2610511023"
username = "siti023"

# Nama disimpan dalam huruf kecil
name = full_name.lower()

# Mengambil tahun angkatan dari NIM
intake = "20" + nim[:2]

# Membuat kartu mahasiswa
print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)

print(f"{'Name':<10}: {name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: {intake}")

print("=" * 30)