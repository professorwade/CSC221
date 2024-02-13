import random

def menu():
    print("""
    A. Drink from your canteen.
    B. Ahead moderate speed.
    C. Ahead full speed.
    D. Stop and rest.
    E. Status check.
    Q. Quit.
    
    """)

def main():

    drinks_in_canteen = 3
    natives_distance = -20
    players_distance = 0
    camel_tiredness = 0

    playing = True
    while playing:
        menu()
        choice = input("You choice? ").lower()
        if choice == 'q':
            playing = False
            continue
        elif choice == 'a':
            drinks_in_canteen -= 1
            natives_distance += 5;
            pass #drink from canteen
        elif choice == 'b':
            pass # ahead moderate speed
        elif choice == 'c':
            pass # ahead full speed
        elif choice == 'd':
            pass # stop and rest
        elif choice == 'e':
            pass # status check
        else:
            print("Please choose a valid option!")


main()
