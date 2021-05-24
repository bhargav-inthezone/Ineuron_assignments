''' Quesiton 1) Write a program to convert Kilometers to miles?'''

kilometers = float(input("Enter kilometer value:"))
miles = 0
def km_to_miles(kms):
    mile = 1.60934*kms
    return mile

print("Kilometers = ", kilometers, "\nMiles = ", km_to_miles(kilometers))

