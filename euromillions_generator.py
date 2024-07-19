import random

def generate_euromillions_numbers():
    main_numbers = random.sample(range(1, 51), 5)
    lucky_stars = random.sample(range(1, 13), 2)
    return main_numbers, lucky_stars

if __name__ == "__main__":
    main_numbers, lucky_stars = generate_euromillions_numbers()
    print("Your Euromillions numbers are:", main_numbers)
    print("Your Lucky Stars are:", lucky_stars)

