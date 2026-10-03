print("==== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ====")
x_3021 = int(input("Masukkan ukuran skala jam pasir (N): "))

# ---------- Bingkai atas ----------
print("#", end="")
for garis_3021 in range(4 * x_3021 + 5):
    print("=", end="")
print("#")

# ---------- Fase 1: jam pasir atas (baris N turun s.d. 1) ----------
for baris_3021 in range(x_3021, 0, -1):
    print("|", end="")
    print(" ", end="")
    # spasi penyeimbang kiri
    for spasi_kiri_3021 in range(2 * (x_3021 - baris_3021)):
        print(" ", end="")
    # deret angka mundur (baris -> 1)
    for angka_mundur_3021 in range(baris_3021, 0, -1):
        print(angka_mundur_3021, end=" ")
    # poros kristal
    print("<*>", end="")
    # deret angka maju (1 -> baris)
    for angka_maju_3021 in range(1, baris_3021 + 1):
        print(" ", end="")
        print(angka_maju_3021, end="")
    # spasi penyeimbang kanan
    for spasi_kanax_3021 in range(2 * (x_3021 - baris_3021)):
        print(" ", end="")
    print(" ", end="")
    print("|", end="")
    print()

# ---------- Fase 2: poros titik pusat ----------
print("|", end="")
for spasi_kiri_3021 in range(2 * x_3021 + 1):
    print(" ", end="")
print("<*>", end="")
for spasi_kanax_3021 in range(2 * x_3021 + 1):
    print(" ", end="")
print("|", end="")
print()

# ---------- Fase 3: jam pasir bawah (baris 1 naik s.d. N) ----------
for baris_3021 in range(1, x_3021 + 1):
    print("|", end="")
    print(" ", end="")
    # spasi penyeimbang kiri
    for spasi_kiri_3021 in range(2 * (x_3021 - baris_3021)):
        print(" ", end="")
    # deret angka mundur (baris -> 1)
    for angka_mundur_3021 in range(baris_3021, 0, -1):
        print(angka_mundur_3021, end=" ")
    # poros kristal
    print("<*>", end="")
    # deret angka maju (1 -> baris)
    for angka_maju_3021 in range(1, baris_3021 + 1):
        print(" ", end="")
        print(angka_maju_3021, end="")
    # spasi penyeimbang kanan
    for spasi_kanax_3021 in range(2 * (x_3021 - baris_3021)):
        print(" ", end="")
    print(" ", end="")
    print("|", end="")
    print()

# ---------- Bingkai bawah ----------
print("#", end="")
for garis_3021 in range(4 * x_3021 + 5):
    print("=", end="")
print("#")