# rock paper scissors games
import random

# Scissors
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

# Paper
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Rock
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

print(rock)
print(paper)
print(scissors)

users_choice = int(input("enter your choice '0' for Rock '1' for paper and '2' for scissors \n  "))

computer_choice = random.randint(0,2)
print(f"computer choice {computer_choice}")
if users_choice == computer_choice :
    print("its a draw")
    
elif users_choice == 0 and  computer_choice == 2 :
     print(f"You Win")
elif users_choice > computer_choice :
        print(f"You Win")
else:
     print(f"You Loose")
    