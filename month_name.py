# Prompt user for a month number
month_num = int(input("Enter a month number (1-12): "))

# Determine month name using if/elif/else statements
if month_num == 1:
    month = "January"
elif month_num == 2:
    month = "February"
elif month_num == 3:
    month = "March"
elif month_num == 4:
    month = "April"
elif month_num == 5:
    month = "May"
elif month_num == 6:
    month = "June"
elif month_num == 7:
    month = "July"
elif month_num == 8:
    month = "August"
elif month_num == 9:
    month = "September"
elif month_num == 10:
    month = "October"
elif month_num == 11:
    month = "November"
elif month_num == 12:
    month = "December"
else:
    month = None

# Print result or error message
if month:
    print("Month is:")
    print(month)
else:
    print("Error: Invalid month number. Please enter a number between 1 and 12.")