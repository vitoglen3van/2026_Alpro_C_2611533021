kalimat = input("Masukkan kalimat: ")

# Menghilangkan spasi dan mengubah huruf menjadi kecil
clean = kalimat.replace(" ", "").lower()

# Memeriksa palindrom
if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")