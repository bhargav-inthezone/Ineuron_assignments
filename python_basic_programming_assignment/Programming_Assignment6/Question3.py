'''Question3)Write a program to calculate Body Mass Index?'''
mass = float(input("Enter weight in kilograms:"))
height = float(input("Enter height in centimeter:"))
height = height/100
BMI = mass/(height**2)
print("Your BMI_INDEX = ",BMI)