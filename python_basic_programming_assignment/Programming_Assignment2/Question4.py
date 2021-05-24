'''Question 4) Write a program to solve quadratic equation?'''
import math

a = int(input("Enter coeffient of x^2 which should be greater than 0 :"))
b = int(input("Enter coefficient of x:"))
c = int(input("Enter the constant value:"))

def quadratic_expre_roots(a,b,c):

    #Discremenant
    discremenant = (b^2)- 4*a*c
    sqrt_discremenant = math.sqrt(abs(discremenant))

    #Check discremenant condition
    if discremenant<0:
        print("Complex Roots") 
        print("x1= ", - b / (2 * a), " + i", sqrt_discremenant) 
        print("x2= ", - b / (2 * a), " - i", sqrt_discremenant)

    elif discremenant==0:
        print(" real and same roots = ") 
        print(-b / (2 * a)) 

    else:
        print(" real and different roots ") 
        print(("x1= ", -b + sqrt_val)/(2 * a)) 
        print(("x2= ", -b - sqrt_val)/(2 * a))


if a==0:
    print("Entered value shall not be 0")

else:
    quadratic_expre_roots(a,b,c)
    

    
    