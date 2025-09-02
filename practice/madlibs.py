# Madlibs
# Create a random story utilizing custom adjectives within placeholders in specific spots in the story

def main():
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    adjective2 = input("Enter an adjective: ")
    adjective3 = input("Enter an adjective: ")

    print(f"Today I went to a(n) {adjective1} zoo.")
    print(f"In an exhibit, I saw a {noun1}.")
    print(f"{noun1} was {adjective2} and {verb1}.")
    print(f"I was {adjective3}!")


if __name__ == "__main__":
    main()