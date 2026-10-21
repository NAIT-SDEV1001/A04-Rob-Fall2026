import squares_calculator

try:
    my_square = int(input("Enter a positive whole number to sum the squares: "))

    if my_square < 1:
        print("Error: Enter a positive integer to square. Example: 3")
    else:
        total = squares_calculator.calculate_sum_of_squares(my_square)

        print(f"The sum of squares is: {total}")
except ValueError:
    print("Error: Enter a positive integer to square. Example: 3")