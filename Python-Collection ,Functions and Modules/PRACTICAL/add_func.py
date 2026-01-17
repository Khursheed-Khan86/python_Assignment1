#Write a Python program to create a parameterized function that takes two arguments and prints their sum.
def add(num1,num2):
    print(f"{num1} + {num2} = {num1+num2}")
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
add(num1,num2)