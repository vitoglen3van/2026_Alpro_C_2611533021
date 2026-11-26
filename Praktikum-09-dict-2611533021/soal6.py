# Data jadwal kuliah
schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"]
}

# 6a. Mencari hari dengan mata kuliah terbanyak
busiest_day = max(schedule, key=lambda day: len(schedule[day]))

print("Busiest day:", busiest_day,
      f"({len(schedule[busiest_day])} courses)")

# 6b. Meminta input nama mata kuliah
course = input()

# Menghitung jumlah hari mata kuliah muncul
count = 0

for day in schedule:
    if course in schedule[day]:
        count += 1

print(f"{course}: {count} days")