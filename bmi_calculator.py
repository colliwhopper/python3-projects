#!/usr/bin/env python3

weight = int( input("enter your weight in kg: ") )
height = float( input("enter your height in m: ") )
bmi = format( int(weight / height ** 2), '.2f' )
