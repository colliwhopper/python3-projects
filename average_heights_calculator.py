#!/usr/bin/env python3

student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_heights=0
for h in student_heights:
  total_heights = total_heights+h

count=0
for c in student_heights:
  count = count+1

average_height = round(total_heights/count)

print( "average height is: " + str(average_height) + "cm" )
