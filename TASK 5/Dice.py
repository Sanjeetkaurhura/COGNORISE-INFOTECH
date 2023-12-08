import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Dice Rolling Simulator!")

    while True:
        input("Press Enter to roll the dice...")

        # Roll the dice
        result = roll_dice()

        print(f"You rolled a {result}!")

        play_again = input("Do you want to roll again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
