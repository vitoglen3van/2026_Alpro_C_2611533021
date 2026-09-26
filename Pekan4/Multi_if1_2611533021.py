umur_3021 = int(input("Input umur anda: "))
sim_3021 = input("Apakah anda sudah punya sim C (y/t): ")[0]

if umur_3021 >= 17 and sim_3021 == 'y':
    print("Anda sudah dewasa dan boleh bawa motor")

if umur_3021 >= 17 and sim_3021 != 'y':
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")

if umur_3021 < 17 and sim_3021 == 'y':
    print("Anda belum cukup umur untuk punya SIM")

if umur_3021 < 17 and sim_3021 != 'y':
    print("Anda belum cukup umur bawa motor")