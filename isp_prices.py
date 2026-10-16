# isp_prices.py

package = input("Enter the package: ").upper()
hours_used = float(input("Enter the number of hours used: "))

if package == "A":
    total_price = 9.95

    if hours_used > 10:
        total_price += (hours_used - 10) * 2.00

elif package == "B":
    total_price = 13.95

    if hours_used > 20:
        total_price += (hours_used - 20) * 1.00

elif package == "C":
    total_price = 19.95

else:
    print("Invalid package.")
    quit()

print("The total price is $" + str(round(total_price, 2)))