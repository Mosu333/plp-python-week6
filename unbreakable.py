def ask_for_number(prompt):
    """Keep asking until the user types a whole number."""
    while True:
        text = input(prompt)
        try:
            return int(text)
        except ValueError:
            # Bad input: it cannot be turned into a number at all
            print("That is not a number. Try again.")


def main():
    while True:
        age = ask_for_number("Enter your age (or 0 to quit): ")

        if age == 0:
            print("Goodbye!")
            break

        # Unwise input: it is a number, but it makes no sense as an age
        if age < 0 or age > 120:
            print("That age is not realistic. Try again.")
            continue

        print(f"Next year you will be {age + 1}.")


main()
