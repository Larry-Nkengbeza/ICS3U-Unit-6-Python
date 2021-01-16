# usr/bin/env Python
# This program was created on January 2021
# This program was created by Larry Nkengbeza
# This program calculates the total numbers

import random


def main():

    # Input
    random_numbers = [random.randint(0, 9),
                      random.randint(0, 9),
                      random.randint(0, 9),
                      random.randint(0, 9),
                      random.randint(0, 9),
                      random.randint(0, 9),
                      random.randint(0, 9),
                      random.randint(0, 9),
                      random.randint(0, 9),
                      random.randint(0, 9)]
    # Output
    print(random_numbers)
    print("The answer is {}", sum(random_numbers))


if __name__ == "__main__":
    main()
