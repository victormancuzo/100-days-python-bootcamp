import random

from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

lives = 6

chosen_word = random.choice(word_list)
# print(chosen_word)

word_length = len(chosen_word)

display = ["_"] * word_length
print("".join(display))

game_over = False
guessed_letters = []

while not game_over:
    print(
        f"****************************{lives}/6 LIVES LEFT****************************"
    )
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You've already guessed \"{guess}\". Try again!")
        continue

    guessed_letters.append(guess)

    for i in range(word_length):
        if chosen_word[i] == guess:
            display[i] = guess

    print(f"Word to guess: {"".join(display)}")

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
