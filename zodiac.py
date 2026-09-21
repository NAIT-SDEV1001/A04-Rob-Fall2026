# Prompt the user to enter a year
year = int(input("Enter a year: "))

# Calculate the remainder when dividing by 12
zodiac_index = year % 12

# Determine the Chinese Zodiac animal based on the remainder
if zodiac_index == 0:
    print("monkey")
elif zodiac_index == 1:
    print("rooster")
elif zodiac_index == 2:
    print("dog")
elif zodiac_index == 3:
    print("pig")
elif zodiac_index == 4:
    print("rat")
elif zodiac_index == 5:
    print("ox")
elif zodiac_index == 6:
    print("tiger")
elif zodiac_index == 7:
    print("rabbit")
elif zodiac_index == 8:
    print("dragon")
elif zodiac_index == 9:
    print("snake")
elif zodiac_index == 10:
    print("horse")
elif zodiac_index == 11:
    print("sheep")