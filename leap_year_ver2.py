user_input = input("Enter a year: ")
year_guess = int(user_input)

if year_guess % 400 == 0:
    is_leap_year = True
elif year_guess % 100 == 0:
    is_leap_year = False
elif year_guess % 4 == 0:
    is_leap_year = True
else:
    is_leap_year = False

print(f"Is {year_guess} a leap year? {is_leap_year}")