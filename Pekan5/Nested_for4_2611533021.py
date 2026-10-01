tinggi_3021 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_3021 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_3021 = tinggi_3021
    c_3021 = a_3021
    lebar_3021 = (2 * tinggi_3021) - 2

    for i_3021 in range(1, tinggi_3021 + 1):
        b_3021 = c_3021 + 1

        for j_3021 in range(1, lebar_3021 + 1):

            # Baris atas dan bawah
            if i_3021 == 1 or i_3021 == tinggi_3021:
                if j_3021 == 1 or j_3021 == lebar_3021:
                    print("#", end="")
                else:
                    print("=", end="")
            # Baris isi
            else:
                if j_3021 == 1 or j_3021 == lebar_3021:
                    print("|", end="")
                else:
                    if j_3021 == c_3021:
                        print("<", end="")
                    elif j_3021 == b_3021:
                        print(">", end="")
                    elif j_3021 == (lebar_3021 - c_3021):
                        print("<", end="")
                    elif j_3021 == (lebar_3021 - c_3021 + 1):
                        print(">", end="")
                    elif j_3021 > b_3021 and j_3021 < (lebar_3021 - c_3021):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        #Logika asli java
        a_3021 -= 2

        if a_3021 <= 0:
            c_3021 = (-a_3021) + 2
        else:
            c_3021 = a_3021