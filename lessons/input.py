# Input
# Prompt the user to receive input

def calculate_area():
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    return length * width


def purchase():
    item = input("What item would you like to purhcase? ")
    price = float(input("What is the price? "))
    quantity = int(input("How many of the item would you like? "))

    return price * quantity, item


def main():
    name = input("What is your name? ") # Returns user data as a string
    age = int(input("How old are you? ")) # Returns user data as a string
    print(f"Hello {name}!")
    print(f"You are {age} years old")

    age = int(age) + 1

    print(f"Next year, you will be {age} years old!")
    print(type(age))

    area = calculate_area()
    print(f"The area is {area}u^2")

    cost, item = purchase()
    print(f"The {item} you purchased cost a total of ${cost}.")


if __name__ == "__main__":
    main()