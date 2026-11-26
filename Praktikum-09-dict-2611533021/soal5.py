pay_times = int(input())
payment_data = {}

for i in range(pay_times):
    temp = input().split() # temp is a list
    if temp[0] not in payment_data:
        payment_data[temp[0]] = int(temp[1])
    else:
        payment_data[temp[0]] += int(temp[1])

total = 0
top_contributor = ""
highest = 0
for name in payment_data:
    total += payment_data[name]
    if payment_data[name] > highest:
        highest = payment_data[name]
        top_contributor = name
    print(f"{name}: {payment_data[name]}")
print("Total cash: ", total)
print(f"Top contributor: {top_contributor} ({highest})")