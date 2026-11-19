menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []

# Membaca data penjualan
for day in range(number_of_days):
    row = []
    for menu in menus:
        amount = int(input(f"Day {day+1}, {menu}: "))
        row.append(amount)
    sales.append(row)

# Total penjualan setiap hari
print("Total per day:")
for i, row in enumerate(sales):
    total = 0
    for amount in row:
        total += amount
    print(f"Day {i+1}: {total}")

# Total penjualan setiap menu
menu_totals = []

for j, name in enumerate(menus):
    total = 0
    for i in range(number_of_days):
        total += sales[i][j]
    menu_totals.append((name, total))

print("Total per menu:", menu_totals)

# Mencari menu terlaris
best_name = ""
best_total = -1

for name, total in menu_totals:
    if total > best_total:
        best_total = total
        best_name = name

print(f"Best seller: {best_name} ({best_total})")