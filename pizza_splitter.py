print ("Pizza Splitter Program")

try:
    cost = float(input("Enter the cost of the pizza: "))
    people = int(input("Enter the number of people: "))
    cost_per_person = cost / people

except ValueError:
    print("Enter a numeric cost for pizza and a whole number for people")
except ZeroDivisionError:
    print("You cannot split the cost among zero people.")
else: #this else only runs if no errors occured
    print(f"Cost per person: ${cost_per_person:.2f}")

print("\npizza_splitter program ended")
