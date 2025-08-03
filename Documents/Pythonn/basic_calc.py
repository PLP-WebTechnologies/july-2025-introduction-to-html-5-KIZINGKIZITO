#Ask the user to input the first number.
num1 = float(input("input the first numbe:"))

#Ask the user to input the second number.
num2 = float(input("input the second number:"))

#Ask trhe user to input an operation

operation = (input("enter an operation (+, -, *, /): "))

# Computing.
#Addition.
if operation == '+':
    result = num1 + num2
    print(f"{num1}+{num2}={result}")

#Subtraction.
elif operation == '-':
    result = num1 - num2 
    print(f"{num1}-{num2}={result}")

#Multiplication.
elif operation == '*':
    result = num1 * num2
    print(f"{num1}*{num2}={result}")

#Divislion.
elif operation == '/':
    if num2 == 0:
       print("Math error: division by 0 not allowed!")

    else:
     result = num1 / num2
    print(f"{num1} / {num2} = {result}")


else:
    print("Invalid operation! Please enter one of: +, -, *, /")