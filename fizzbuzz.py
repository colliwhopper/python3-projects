#!/usr/bin/env python3

for n in range(1, 101):
  if int(n%3==0 and n%5==0):
    print("FizzBuzz")
  elif int(n%3==0):
    print("Fizz")
  elif int(n%5==0):
    print("Buzz")
  else:
    print(n)
