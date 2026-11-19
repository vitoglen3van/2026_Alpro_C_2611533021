number_of_rows = 4
seats_per_row = 5
# Write your code below
seats = [['.' for _ in range(seats_per_row)] for _ in range(number_of_rows)]

while True:
    for i in range(number_of_rows):
        print(f"Row {i + 1}: {' '.join(seats[i])}")
    
    row = int(input("Row (0 to stop): "))
    if row == 0:
        break
    
    seat = int(input("Seat: "))
    
    if row < 1 or row > number_of_rows or seat < 1 or seat > seats_per_row:
        print("Invalid seat.")
    elif seats[row - 1][seat - 1] == 'X':
        print("Seat already taken.")
    else:
        seats[row - 1][seat - 1] = 'X'
        print("Seat booked.")

taken_count = sum(row.count('X') for row in seats)
print(f"Seats taken: {taken_count}")