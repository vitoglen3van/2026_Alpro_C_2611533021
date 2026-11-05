height = int(input("Masukkan tinggi: "))

for row in range(1, height + 1):
    for column in range(1, height - row + 2):
        print("*", end=" ")
    print()