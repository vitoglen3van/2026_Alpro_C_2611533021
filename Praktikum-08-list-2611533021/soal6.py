LAST_DIGIT = 3
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []

# Memasukkan pengeluaran selama 7 hari
for day in range(1, 8):
    amount = int(input(f"Day {day}: "))
    expenses.append(amount)

# Menghitung total
total = 0
for amount in expenses:
    total += amount

# Menghitung rata-rata
average = total / 7

# Mencari pengeluaran tertinggi
highest = expenses[0]
highest_day = 1

for i in range(7):
    if expenses[i] > highest:
        highest = expenses[i]
        highest_day = i + 1

# Menghitung hari di atas batas
days_above = 0
for amount in expenses:
    if amount > daily_limit:
        days_above += 1

# Menampilkan hasil
print("Daily limit:", daily_limit)
print("Total:", total)
print("Average:", round(average, 1))
print(f"Highest: day {highest_day} ({highest})")
print("Days above limit:", days_above)