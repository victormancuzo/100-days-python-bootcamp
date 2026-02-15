import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("Rock paper scissors!")

options = ["Rock", "Paper", "Scissors"]
art = [rock, paper, scissors]

player_choice = int(input(
    "What do you choose? Type 0 for rock, 1 for paper or 2 for scissors: "
))
print("\nYou chose:")
print(art[player_choice])
player_choice = options[player_choice]

cpu_choice = random.randint(0, 2)
print("\nCPU chose:")
print(art[cpu_choice])
cpu_choice = options[cpu_choice]

if player_choice == cpu_choice:
    print("Draw!")
elif player_choice == "Rock":
    if cpu_choice == "Scissors":
        print("You win!")
    else:
        print("You lose!")
elif player_choice == "Paper":
    if cpu_choice == "Rock":
        print("You win!")
    else:
        print("You lose!")
elif player_choice == "Scissors":
    if cpu_choice == "Paper":
        print("You win!")
    else:
        print("You lose!")
