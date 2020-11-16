# Python Program to find Factorial of a Number

number = int(input(" Please enter any Number to find factorial : "))
fact = 1
i = 1

while(i <= number):
    fact = fact * i
    i = i + 1

print("The factorial of %d  = %d" %(number, fact))