"""
Programmer: Sidd
Program: bounces.py
Project 1.3

This program calculates the total distance a ball travels as it bounces
1. the initial height of the ball
2. bounciness index
3. the number of times the ball is allowed to continue bouncing
"""
#Input drop height
dropHeight = float(input("Enter drop height: "))
bounciness = 0.6
distance = 0
bounces = int(input("Enter bounces here: "))

#For loop for calculations
for eachPass in range(bounces):
    distance += dropHeight
    dropHeight *= bounciness
    distance += dropHeight


#Output total distance traveled
print("The total distance traveled is:", distance, "feet")