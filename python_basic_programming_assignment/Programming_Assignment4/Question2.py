'''Question2 ) Write program to display multipliction table?'''
number = int(input("Enter a number:"))
max_table_value= int(input("Enter the max table value: "))
print("Table ",number,":")
for i in range(1,max_table_value+1):
    print(" ", number,"*",i," = ", number*i)
    