def add(a,b):
    answer=a+b
    return answer

def Subtract(a,b):
    answer=a-b
    return answer

def division(a,b):
    answer=a/b
    return answer

def multiply(a,b):
    answer=a*b
    return answer

def remainder(a,b):
    answer=a%b
    return answer

def intdivision(a,b):
    answer=a//b
    return answer

def exponential(a,b):
    answer= a**b
    return answer

def square(a):
    answer=a*a
    return answer

def cube(a):
    answer=a*a*a
    return answer

def factorial(a):
    fact =1
    for num in range (1, a+1):
        fact *=num
    return fact
