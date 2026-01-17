#Write a Python program to create a calculator using functions. 
menu="""
    Press 1 for Addition.
    Press 2 for Subtraction.
    Press 3 for Multiplicaion
    Press 4 for Division
"""
print(menu)
def Addition(num1,num2):
   result=num1+num2
   return result
def Subtract(num1,num2):
    result=num1-num2
    return result
def Multiply(num1,num2):
    result=num1*num2
    return result
def Divide(num1,num2):
    result=num1/num2
    return result
try:
    choice=int(input("Enter your choice: "))
    if choice in (1,2,3,4):
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second numer: "))
    if choice==1:
        print(f"Addition of {num1} and {num2} is ",Addition(num1,num2))
    elif choice==2:
         print(f"Subtraction of {num1} and {num2} is ",Subtract(num1,num2))
    elif choice==3:
        print(f"Multiplication of {num1} and {num2} is ",Multiply(num1,num2))
    elif choice==4:
        print(f"Division of {num1} and {num2} is ",Divide(num1,num2))
    else:
        print("Invalid choice")
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(e)