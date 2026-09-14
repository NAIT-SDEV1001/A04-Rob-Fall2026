# Temp conversion program

celcius_input = float(input("Enter temperature in celcius: "))
fahrenheit_equivalent = (celcius_input * 9/5) + 32
print(f"{celcius_input} celcius converted to fahrenheit is: {fahrenheit_equivalent}")

# Print a silly sentence program

name = input("Enter a name: ")
adjective = input("Enter an adjective: ")
verb = input("Enter a past-tense verb: ")
place = input("Enter a place: ")

print(f"{name} the {adjective} penguin {verb} all the way to {place}")

# Rectangle calculator program

width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of the rectangle: "))
area = width * height
perimeter = 2 * (width  + height)

print(f"Width: {width:.3f} and the height is {height:.3f}")
print(f"Area: {area:.3f}")
print(f"Perimeter: {perimeter:.3f}")

# GST calculator program

price = float(input("Enter the price of the item: $"))
quatity = int(input("Enter the quantity purchased: "))
subtotal = price * quatity
gst = subtotal * 0.05
total = subtotal + gst

print(f"Subtotal: ${subtotal}")
print(f"GST (5%): ${gst}")
print(f"Total: ${total}")

# Miles to Kilometers converter program

miles = float(input("Enter the number of miles: "))
kilometers = miles * 1.609344
print(f"{miles:.2f} miles is equal to {kilometers:.2f} kilometers.")

# Trip Cost calculator program

distance = float(input("Enter the distance to travel (km): "))
fuel_consumption = float(input("Enter the fuel consumption (L/100 km): "))
price_per_litre = float(input("Enter the price per litre: $ "))
fuel_used = (distance / 100) * price_per_litre
trip_cost = fuel_used * price_per_litre

print(f"Distance: {distance:.2f} km")
print(f"Fuel Used: {fuel_used:.2f} L")
print(f"Trip Cost: ${trip_cost:.2f}")