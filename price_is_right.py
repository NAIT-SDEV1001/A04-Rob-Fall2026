import random

prices = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]

print("Welcome to the Price is Right! Guess the price of this coffee")

guess = int(input("Guess the price of the item: "))

if guess in prices:
    print("You win!")
else:
    print("You lose!")

print(f"The prices were: {prices}")
