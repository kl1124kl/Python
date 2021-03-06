__author__ = "Jiaqi Li"
import cmath

#definitions for the five math operations
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a*b
# for the quadratic formula, there can be two cases for the numerator
def quadratic(a,b,c):
    case1 = (b*-1 + cmath.sqrt(b**2 - 4*a*c))/(2*a)
    case2 = (b*-1 - cmath.sqrt(b**2 - 4*a*c))/(2*a)
    return case1,case2
   
#if the user enters a valid specified symbol, perform one of the operation accordingly. 
def calculator(user_operation, a, b, c=None):
    if user_operation == "quad":
        x1,x2 = quadratic(a,b,c)
        return x1,x2
    elif user_operation == "+" :
        x= addition(a,b)
    elif user_operation == "-":
        x=subtraction(a,b)
    elif user_operation == "*":
        x=multiplication(a,b)
    elif user_operation == "/":
        x=division(a,b)
    return x




def main():
    user_operation = input("What operation would you like to perform? Enter + for addition, - for subtraction,\
        * for multiplication, / for division, quad to solve a quadratic equation, or q to quit")  
  
        #if the user wants to solve a quadratic equation, ask them to input three variables,represented by a, b, and c. Otherwise, only input two numbers
    while user_operation != 'q':
       
        if user_operation == "quad":
            a = int(input("Enter the first number, representing the value of a in a quadratic equation."))
            b = int(input("Enter the second number, representing the value of b in a quadratic equation."))
            c = int(input("Enter the third number, representing the value of c in a quadratic equation."))
            x1,x2 = calculator(user_operation,a,b,c)
            print(x1,x2)
        elif user_operation == "+" or user_operation == "-" or user_operation == "*" or user_operation == "/":
            a = int(input("Enter the first number"))
            b = int(input("Enter the second number"))
            x = calculator(user_operation,a,b)
            print(x)
            #if the user enters an invalid operation symbol, print the error message and terminate the program
        else:
            print("Error! Invalid operation choice")
        
        user_operation = input("What operation would you like to perform? Enter + for addition, - for subtraction,\
                * for multiplication, / for division, quad to solve a quadratic equation, or q to quit")
main()
