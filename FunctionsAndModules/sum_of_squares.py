from squares_calculator import calculate_sum_of_squares
# vs 
# import squares_calculator

# use the second method when all functions of the module are being used
# but you must prefix function calls with module name (i.e. squares_calculator.function)
# so line 15 would need to change

try:
    my_square = int(input("Enter a positive whole number to sum the squares: "))

    if my_square < 1:
        print("Error: Enter a positive integer to square. Example: 3")
    else:
        total = calculate_sum_of_squares(my_square)

        print(f"The sum of squares is: {total}")
except ValueError:
    print("Error: Enter a positive integer to square. Example: 3")