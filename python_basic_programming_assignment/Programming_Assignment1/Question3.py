''' Question 3)Write a program find the area of a triangle?'''

base = int(input("Enter the base value :"))
height= int(input("Enter the height value:"))

def Area_of_Triangle(x,y):
    Area = 1/2*(x*y)
    return Area

print("Area of Triangle =", Area_of_Triangle(base,height))