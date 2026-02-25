import random

from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

lives = 6

chosen_word = random.choice(word_list)
# print(chosen_word)

placeholder = "_" * len(chosen_word)
print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(
        f"****************************{lives}/6 LIVES LEFT****************************"
    )
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed \"{guess}\". Try again!")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(f"Word to guess: {display}")

    if guess not in chosen_word:
        print(
            f"You guessed: {guess}, that's not in the word. You lose a life."
        )
        lives -= 1

        if lives == 0:
            game_over = True
            print(
                f"\n***********************THE WORD WAS \"{chosen_word}\"! YOU LOSE**********************"
            )

    if "_" not in display:
        game_over = True
        print("\n****************************YOU WIN****************************")

    print(stages[lives])
