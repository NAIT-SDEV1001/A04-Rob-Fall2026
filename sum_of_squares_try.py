
try:
    my_square = int(input("Enter a positive whole number to sum the squares: "))

    if my_square < 1:
        print("Error: Enter a positive integer to square. Example: 3")
    else:
        total = 0

        for number in range(1, my_square +1):
            total = total + (number * number)

        print(f"The sum of squares is: {total}")
except ValueError:
    print("Error: Enter a positive integer to square. Example: 3")