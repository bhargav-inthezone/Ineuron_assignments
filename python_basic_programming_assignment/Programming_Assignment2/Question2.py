''' Question 2) Write a program to convert Celsius to Fahrenheit?'''

cel = float(input("Enter Celsius recording:"))

def celsius_to_Fahrenheit(celsius):
    Fahrt = ((celsius*9)/5)+32
    return Fahrt
print("Celsius Value = ", cel, "\nFahrenheit Value = ",celsius_to_Fahrenheit(cel))
