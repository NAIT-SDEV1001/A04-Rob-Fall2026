my_square = int(input("Enter a number to sum the squares: "))

total = 0

for number in range(1, my_square +1):
    total = total + (number * number)

print(f"The sum of squares is: {total}")