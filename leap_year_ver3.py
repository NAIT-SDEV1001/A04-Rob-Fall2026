user_input = input("Enter a year: ")
year_guess = int(user_input)

# Stage 1: Check if it's a century year (ends in 00)
if year_guess % 100 == 0:
    # Stage 2a: Century years must be divisible by 400
    if year_guess % 400 == 0:
        is_leap_year = True
    else:
        is_leap_year = False
else:
    # Stage 2b: Non-century years must be divisible by 4
    if year_guess % 4 == 0:
        is_leap_year = True
    else:
        is_leap_year = False

print(f"Is {year_guess} a leap year? {is_leap_year}")