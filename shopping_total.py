print ("Shopping total program...")

item_count = 0
total_cost = 0
price_input = input("Enter an item price (q to quit): ")

while price_input.lower() != "q":
    price = float(price_input)
    total_cost += price
    item_count += 1
    price_input = input("Enter an item price (q to quit): ")

print(f"Number of items purchased: {item_count}")
print(f"Total cose: ${total_cost:.2f}")

# add exception handling to the above