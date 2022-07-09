import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
players = int((len(names)))
payer = print( names[random.randint(0, int(players))] + " is going to buy the meal today!" )


#nasty 2-line version:
# names_string = input("Give me everybody's names, separated by a comma. ")
# payer = print( names_string.split(", ")[random.randint(0, int((len(names_string.split(", ")))))] + " is going to buy the meal today!" )

#using the random module "choice" parameter:
# import random
#
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# payer = random.choice(names)
#
# print( payer + " is going to buy the meal today!" )
