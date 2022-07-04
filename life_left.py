#!/usr/bin/env python3

age = input("What is your current age?")

months = 12 * 90 - int(age) * 12
weeks = 52 * 90 - int(age) * 52
days = 365 * 90 - int(age) * 365

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
