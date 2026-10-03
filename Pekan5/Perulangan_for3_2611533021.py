ulang_3021 = int(input("Masukkan jumlah_3021 pengulangan: "))

jumlah_3021 = 0
for i_3021 in range(1, ulang_3021 + 1):
    print(i_3021, end=" ")
    jumlah_3021 = jumlah_3021 + i_3021

    if i_3021 < ulang_3021:
        print("+", end=" ")
    else:
        print("= ", jumlah_3021,end=" ")
print()
print("jumlah =", jumlah_3021)