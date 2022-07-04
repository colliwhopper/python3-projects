#!/usr/bin/env python3

print("Welcome to the tip calculator!")

total = float( input("What was the total bill? ") )
tip = int( input("How much tip would you like to give? ") )
split = int ( input("How many people to split the bill? ") )

final_total = round( (total + (total/tip)) / split, 2 )

print(f"Each person should pay: {final_total}")
