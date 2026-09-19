# Input tidak peka terhadap huruf besar dan kecil
a1_3021 = input("Input nilai boolean-1 (true/false): ").strip().lower() == "true"
a2_3021 = input("Input nilai boolean-2 (true/false): ").strip().lower() == "true"

print("\nA1 = ", a1_3021)
print("A2 = ", a2_3021)

# Konjungsi: bernilai True jika keduanya True
hasil = a1_3021 and a2_3021
print("\nKonjungsi (AND)")
print("A1 AND A2 =", hasil)

# Disjungsi: bernilai True jika salah satu True
hasil = a1_3021 or a2_3021
print("\nDisjungsi (OR)")
print("A1 OR A2 =", hasil)

# Negasi: mebalik nilai A1
hasil = not a1_3021
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil)

# Negasi: mebalik nilai A2
hasil = not a2_3021
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil)

# XOR: bernilai True jika kedua nilai berbeda
hasil = a1_3021 != a2_3021
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil)
