# Name: Vito Glenevan
# NIM: 2611533021

# A
username = input("Username: ")

if len(username) < 5:
    print("Invalid: at least 5 characters")
if not username.isalnum():
    print("Invalid: letters and digits only")
if not username[0].isalpha():
    print("Invalid: must start with a letter")
else:
    print("Valid")

# B
nim = input("nim: ")

if len(nim) == 10:
    print("Valid")
if  nim[0].isalpha():
    print("Invalid: must start with a numbers")
else:
    print("Invalid: must atleast 10 number")