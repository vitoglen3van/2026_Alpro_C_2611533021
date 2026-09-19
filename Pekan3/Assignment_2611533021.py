angka1_3021 = int(input("Input angka-1: "))
angka2_3021 = int(input("Input angka-2: "))

print("\nNilai awal angka1 =", angka1_3021)
print("Nilai angka2 =", angka2_3021)

# Assignment biasa
hasil = angka1_3021
print("\nAssignment biasa (=)")
print("Hasil =", hasil)

# Assignment penambahan
hasil = angka1_3021
hasil += angka2_3021
print("\nAssignment penambahan (+=)")
print("Hasil =", hasil)

# Assignment pengurangan
hasil = angka1_3021
hasil -= angka2_3021
print("\nAssignment pengurangan (-=)")
print("Hasil =", hasil)

# Assignment perkalian
hasil = angka1_3021
hasil *= angka2_3021
print("\nAssignment perkalian (*=)")
print("Hasil =", hasil)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_3021 != 0:
    hasil = angka1_3021
    hasil /= angka2_3021
    print("\nAssignment pembagian (/=)")
    print("Hasil =", hasil)
# Operator tambahan
    hasil = angka1_3021
    hasil //= angka2_3021
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil)
    hasil = angka1_3021
    hasil %= angka2_3021
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0")


# Operator tambahan: assignment perpangkatan
hasil = angka1_3021
hasil **= angka2_3021
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil)