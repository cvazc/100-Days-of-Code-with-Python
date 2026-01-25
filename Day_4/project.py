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
---'    ____)____
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

game_images = [rock, paper, scissors]

option = int(
    input("What do you choose? Type '0' for Rock, '1' for Paper or '2' for Scissors: ")
)
computer = random.randint(0, 2)

print(f"COMPUTER {game_images[computer]}")
print(f"YOU {game_images[option]}")

if option == computer:
    print("Tie 🤝")
elif option == 0 and computer == 2:
    print("You WIN! 🏆")
elif computer == 0 and option == 2:
    print("You LOSE! 💀")
elif computer > option:
    print("You LOSE! 💀")
elif option > computer:
    print("You WIN! 🏆")
else:
    print("Invalid number. You LOSE! 💀")
