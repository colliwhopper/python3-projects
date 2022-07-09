#!/usr/bin/env python3

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

image = [rock, paper, scissors]

player_choice = int(input( "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n" ))
computer_choice = random.randint(0, 2)

if player_choice < 0 or player_choice >= 3:
  print("You typed an invalid number, try again.")
else:
  print( "You")
  print(image[player_choice])
  print("\n")

  print( "Computer" )
  print(image[computer_choice])

  if player_choice == computer_choice:
    print( "You chose the same, it's a draw" )
  elif player_choice == 0 and computer_choice == 2:
    print( "You win!" )
  elif computer_choice == 0 and player_choice == 2:
    print( "You lose :(" )
  elif player_choice > computer_choice:
    print( "You win!" )
  elif computer_choice > player_choice:
    print( "You lose :(" )
  else:
    print("You typed an invalid number, try again.")
