def play_game():
    print(r'''
*******************************************************************************
        |                   |                  |                     |
_________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
        |                `"=._o`"=._      _`"=._                     |
_________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
        |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
_________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
    ''')
    print("Welcome to Treasure Island. 🏝️  Your mission is to find the treasure! 🏴‍☠️\n")
    while True:
        left_right = input('You\'re at a cross road. Where do you want to go? (left/right) ').lower()
        if left_right == 'left':
            print('\nYou reach a lake with an island in the middle.')
            while True:
                wait_swim = input("""Type "wait" to wait for a boat. Type "swim" to swim across. """).lower()
                if wait_swim == 'wait':
                    print("\nYou arrive at the island unharmed. There is a house with 3 doors:")
                    while True:
                        door = input("One red, one yellow and one blue. Which colour do you choose? ").lower()
                        if door == 'red':
                            print("It's a room full of fire. Game over! ☠️\n")
                            break
                        elif door == 'yellow':
                            print('You found the treasure. Congrats, you win! 🏆🏆🏆\n')
                            # exit()
                            break
                        elif door == 'blue':
                            print('You enter a room of beasts. Game over! ☠️\n')
                            break
                        else:
                            print('Wrong input, try again!')
                    break
                elif wait_swim == 'swim':
                    print('You get attacked by an angry crocodile. Game over! 🐊☠️\n')
                    break
                else:
                    print('Wrong input, try again!')
            break
        elif left_right == 'right':
            print("You fell into a hole. Game over! ☠️\n")
            break
        else:
            print("Wrong input! Try again with 'left' or 'right'.")

while True:
    play_game()
    replay = input("Do you want to play again? (Y/N): ").lower()
    if replay != 'y':
        print("Thanks for playing! Goodbye!")
        break