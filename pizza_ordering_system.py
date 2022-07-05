#!/usr/bin/env python3

print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0

if size == "S":
  size = 15
  if add_pepperoni == "Y":
    add_pepperoni = 2
  else:
    add_pepperoni = 0

if size == "M":
  size = 20
  if add_pepperoni == "Y":
    add_pepperoni = 3
  else:
    add_pepperoni = 0

if size == "L":
  size = 25
  if add_pepperoni == "Y":
    add_pepperoni = 3
  else:
    add_pepperoni = 0

if extra_cheese == "Y":
  extra_cheese = 1
else:
  extra_cheese = 0

final_bill = str(size + add_pepperoni + extra_cheese)
print("Total Bill is: £" + final_bill)
