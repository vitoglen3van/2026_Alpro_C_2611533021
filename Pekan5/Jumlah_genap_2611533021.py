ulang_3021 = int(input("Masukkan nilai batas: "))

jumlah_3021 = 0
for i_3021 in range(1, ulang_3021 + 1):
    if i_3021 % 2 == 0:
        print(i_3021, end="")
        jumlah_3021 = jumlah_3021 + i_3021

        if i_3021 < ulang_3021:
            print("+", end="")
        else:
            print("=", jumlah_3021,end="")
print()
print("jumlah_3021 =", jumlah_3021)