import os
import math
from datetime import datetime

def display():
    print("Enter 'help' for view the display again.")
    print("Enter 'history' for view the operation history.")
    print("Enter 'exit' for exiting the program.")

def evaluate(expression):
    print("Expression:", expression)
    operations = ["+", "-", "*", "/", "^", "v"]

    operands = []
    operators = []

    operand = ''
    for char in expression:
        if char.isdigit() or char == '.':
            operand += char
        else:
            if operand:
                operands.append(float(operand))
                operand = ''
            if char in operations:
                operators.append(char)

    if operand:
        operands.append(float(operand))

    i = 0
    while i < len(operators):
        if operators[i] == "*":
            operands[i] *= operands[i + 1]
            operands.pop(i + 1)
            operators.pop(i)
        elif operators[i] == "/":
            operands[i] /= operands[i + 1]
            operands.pop(i + 1)
            operators.pop(i)
        else:
            i += 1

    result = operands[0] 
    for op, operand in zip(operators, operands[1:]):
        if op == "+":
            result += operand
        elif op == "-":
            result -= operand
        elif op == "^":
            result **= operand
        elif op == "v":
            if operand == "v":  
                result = math.sqrt(result)
            else:
                result = operand ** (1/result)
    return result

def clear():
    os.system("cls")

def save_history(operation):
    current_time = datetime.now()
    formated_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
    with open("history.txt", "a") as file:
        file.write(f'{formated_time} : {operation}\n')

def calculator():
    display()
    while True:
        user_input = input("Enter or write 'exit' to exit program:").strip()
        inputs = user_input.lower()
        if inputs == "exit":
            print("Exiting...")
            break

        elif inputs == "help":
            clear()
            display()

        elif inputs == "history":
            with open("history.txt", "r") as file:
                lines = file.readlines()
                last_five_lines = lines[-5:]
                print("Last 5 History:")
                print(''.join(last_five_lines))
        else:
            result = evaluate(user_input)
            if result is not None:
                print("Result", result)
                save_history(user_input)

if __name__ == "__main__":
    clear()
    calculator()
