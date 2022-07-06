#!/usr/bin/env python3

#question
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#true
t = str(name1+name2).lower().count('t')
r = str(name1+name2).lower().count('r')
u = str(name1+name2).lower().count('u')
e = str(name1+name2).lower().count('e')
true = t + r + u + e

#love
l = str(name1+name2).lower().count('l')
o = str(name1+name2).lower().count('o')
v = str(name1+name2).lower().count('v')
e = str(name1+name2).lower().count('e')
love = l + o + v + e

#result
truelove = int(str(true) + str(love))

#calculate compatibility logic
if truelove <= 10 or truelove >= 90:
  print( "Your score is " + str(truelove) + ", you go together like coke and mentos." )
elif truelove >= 40 and truelove <= 50:
  print("Your score is " + str(truelove) + ", you are alright together.")
else:
  print( "Your score is " + str(truelove) + "." )
