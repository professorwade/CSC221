import random


def menu():
    print("""
    A. Drink from your canteen.
    B. Ahead moderate speed.
    C. Ahead full speed.
    D. Stop for the night.
    E. Status check.
    Q. Quit.
    """)

def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")

    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    natives_distance = -20
    canteen_drinks = 3

    done = False
    while not done:
        menu()
        user_choice = input("What is your choice? ").upper()

        if user_choice == 'Q':
            done = True
        elif user_choice == 'A': # A. Drink from your canteen.
            pass
        elif user_choice == 'B': # B. Ahead moderate speed.
            pass


main()