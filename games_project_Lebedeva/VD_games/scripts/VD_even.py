import prompt
import random

def main():
    print("Welcome to the VD-games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    print('Answer "yes" if the number is even, otherwise answer "no".')

    count = 0
    while count < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")

        answer = prompt.string("Your answer: ")

        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        if answer == correct_answer:
            print("Correct!")
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    main()
