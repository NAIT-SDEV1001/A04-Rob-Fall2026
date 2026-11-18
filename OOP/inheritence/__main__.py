from inheritence.animals import Animal, Dog


def main() -> None:
    # create the animals
    dog = Dog("Ranger", "Brown", 4, "Labrador")
    cat = Animal("Soul Destroyer", "Black", 4)
    bird = Animal("Furry Birdy", "Green", 2)

    # add animals to list
    animals = [dog, cat, bird]

    # loop through the attributes and methods of each animal
    for animal in animals:
        print("-----------------")
        print(animal)
        
        animal.make_a_noise()
        animal.move()
        animal.eat()
        print("-----------------")

if __name__ == "__main__":
    main()