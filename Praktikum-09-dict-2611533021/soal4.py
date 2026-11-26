all_students = input("Masukkan nomor absen seluruh kelas: ").split()
submitted_list = input("Masukkan nomor yang mengumpulkan: ").split()

all_set = set(all_students)
submitted_set = set(submitted_list)

submitted_set = all_set & submitted_set
not_submitted = all_set - submitted_set

print("Submitted:", len(submitted_set), "students")
print("Not submitted:", len(not_submitted), "students")

for student in all_students:
    if student in not_submitted:
        print(student)
        not_submitted.remove(student)