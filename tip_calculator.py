#!/usr/bin/env python3

print("Welcome to the tip calculator!")

total = float( input("What was the total bill? £") )
tip = int( input("What % would you like to tip? ") )
split = int ( input("How many people to split the bill? ") )
final_total = round( (total + (total/tip)) / split, 2 )
final_total = "{:.2f}".format(final_total)

print(f"Each person should pay: £{final_total}")
