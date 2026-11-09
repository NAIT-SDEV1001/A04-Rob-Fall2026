# import required classes
from coin_flip_models.coin import Coin

if __name__ == '__main__':
    # instantiate a loonie
    coin1 = Coin("loonie")
    coin2 = Coin("toonie")

    print(f"First coin is a: {coin1}")
    print(f"Second coin is a: {coin2}")

    if coin1 == coin2:
        print("These coins are the same value")
    elif coin1 > coin2:
        print(f"{coin1} is more valuable then {coin2}")
    else:
        print(f"{coin2} is more valuable then {coin1}")
