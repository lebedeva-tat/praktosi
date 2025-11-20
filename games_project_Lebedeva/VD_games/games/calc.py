import random

DESCRIPTION = 'What is the result of the expression?'

def generate_round():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operation = random.choice(['+', '-', '*'])
    question = f"{num1} {operation} {num2}"

    result = 0
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2

    return question, str(result)
