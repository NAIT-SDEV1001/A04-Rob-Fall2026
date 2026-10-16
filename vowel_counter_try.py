# vowel_counter.py

try:
    word = input("Enter a word for us to count vowels: ")

    if not word.isalpha():
        raise ValueError

    vowel_count = 0

    for letter in word:
        print(letter)

        if letter.lower() in "aeiou":
            vowel_count += 1

    print(f"There are {vowel_count} vowels in {word}")

except ValueError:
    print("Please enter a word using letters only.")