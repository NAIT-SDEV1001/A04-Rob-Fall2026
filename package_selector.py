print("Welcome to the Ultimate Gym")
print("Please select a membership package:")
print("- Package A: $40/month, 4 months (short-term package)")
print("- Package B: $55/month, 8 months (standard package)")
print("- Package C: $75/month, 12 months (regular package)")
print("- Package D: $100/month, 12 month (premium package, includes 4 free personal training sessions)\n")

# Prompt user for package choice and convert input to uppercase
choice = input("Enter the package letter (A/B/C/D): ").strip().upper()

# Determine package details using if/elif/else
if choice == "A":
    monthly_fee = 40
    duration = 4
elif choice == "B":
    monthly_fee = 55
    duration = 8
elif choice == "C":
    monthly_fee = 75
    duration = 12
elif choice == "D":
    monthly_fee = 100
    duration = 12
else:
    monthly_fee = None

# Display output or error message
if monthly_fee is not None:
    total_fee = monthly_fee * duration
    print(f"You have selected Package {choice}")
    print(f"Your monthly fee is ${monthly_fee}")
    print(f"Your total fee is ${total_fee}")
else:
    print("Invalid package selection. Please select A, B, C, or D.")