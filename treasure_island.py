print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

turn = input('''
You are washed ashore on the beach. 
To the left you can see palm trees, to the right you see a cliff. 

Which way do you turn? left or right?
''').lower()

if turn == "left":
  boat = input('''
You come to a lake. There is an island in the middle of it.
Do you look for a boat or swim across? Type "boat" or "swim"        
  ''').lower()
  if boat == "boat":
    choice = input('''
You find a boat and arrive on the island unharmed. You see a large structure resembling a temple, with 3 doors.
One red, one yellow and one blue. Which door do you choose to go through? Type "red", "yellow", or "blue".
  ''').lower()
    if choice == "red":
      print(
        "you enter the temple, but fall into a blazing inferno of fire"
      )
    elif choice == "yellow":
      print("yeharr, TREASUREE!!!")
    elif choice == "blue":
      print("You are eaten by island beasts!")
    else:
      print(
        "oh dear, you typed an unknown choice and disappeared, never to be seen again..."
      )
  elif boat == "swim":
    print("Oh no, you were eaten by Pirahnas! :(")
else:
  print("you slipped on the rocks and died a slow and lonely death!")
