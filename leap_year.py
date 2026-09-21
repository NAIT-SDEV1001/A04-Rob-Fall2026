# A year is a leap year if it meets the following standard calendar rules:
# - Divisible by 4: The year must be evenly divisible by 4
# - Except Century Years: If the year is divisible by 100, it is not a leap year...
# - Unless Bivisible by 400: ...unliess it is also evenly divisible by 400


user_input = input("Enter a year: ")
year_guess = int(user_input)

if (year_guess % 4 == 0 and year_guess % 100 != 0) or (year_guess % 400 == 0):
    print(f"Is {year_guess} a leap year? true")
else: 
    print(f"Is {year_guess} a leap year? false")