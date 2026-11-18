# import required classes
from coin_flip_models.coin import Coin

if __name__ == '__main__':
    # instantiate two Coin objects - a loonie and toonie
    object1 = Coin("loonie")
    object2 = Coin("toonie")

    print(f"Object1 is a: {object1}")
    print(f"Object2 is a: {object2}")

    # show off dunder methods
    if object1 == object2:
        print("These coins are the same value")
        coin_to_flip = object1
    elif object1 > object2:
        print(f"{object1} is more valuable than {object2}")
        coin_to_flip = object1
    else:
        print(f"{object2} is more valuable than {object1}")
        coin_to_flip = object2

    # flip the more valuable coin
    
    user_guess = input(
        "Guess the coin flip! Enter heads, tails, or exit (h/t/x): "
        ).lower()

    while user_guess not in ("h", "t", "x"):
        user_guess = input(
            "Invalid choice. Enter h, t, or x: "
        ).lower()

    if user_guess == "x":
        print("Thanks for playing!")
    else:
        coin_flip_result = coin_to_flip.flip()

        print(f"The coin flip was: {coin_flip_result}")

        if ((coin_flip_result == "heads" and user_guess == "h")
                or (coin_flip_result == "tails" and user_guess == "t")):
            print("You guessed correct!")
        else:
            print("You guessed wrong!")
