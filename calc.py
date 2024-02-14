import math

first_num = int(input("Enter the first number:\n"))
operation = input("Enter the operation:\n")
second_num = int(input("Enter the second number:\n"))
def calculation(first_num,operation,second_num):

    if operation == '*':
        result = first_num * second_num
        return result
    elif operation == '/':
        result = first_num / second_num
        return result
    elif operation == '+':
        result = first_num + second_num
        return result
    elif operation == '-':
        result = first_num - second_num
        return result
    elif operation == '^':
        result = first_num ** second_num
        return result
    else:
        return "Please enter a correct operation"

print(calculation(first_num,operation,second_num))
