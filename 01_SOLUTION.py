# Given two numbers a, b where b > a, find the sum of all primes between them:

a = int(input("Enter first Number: "))  
b = int(input("Enter another number: "))  

total = 0  

for i in range(a + 1, b):  
    c = 0  
    for j in range(1, i + 1):  
        if i % j == 0:  
            c += 1  
    if c == 2:  
        total += i  

print("Sum of prime numbers:", total)  
