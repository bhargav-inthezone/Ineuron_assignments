'''Question5) Write a program to Print all Prime Number in an Interval of 1-10000?'''
prime_numbers =[]
for i in range(2,10001):
    rem = 0
    for j in range(2,i):
        if (i%j)==0:
            rem+=1
    if rem==0:
        prime_numbers.append(i)

print(prime_numbers)


