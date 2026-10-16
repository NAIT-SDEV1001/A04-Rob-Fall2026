# vowel_counter.py

word = input("Enter a word for us to count vowels: ")

vowel_count = 0

for letter in word:
    print(letter)

    if letter.lower() in "aeiou":
        vowel_count += 1

print("There are", vowel_count, "vowels in", word)