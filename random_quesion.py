import random


def main():
    def welcome():
        print("Welcome to our app!")

    def get_name():
        name = input("What's your name? ").strip().title()
        firstname = name.split()[0]
        if 2 < len(firstname) < 10:
            print(f"Welcome, {firstname} to our app!")
        else:
            print("Incorrect name")
            exit()
        return firstname

    def get_age(firstname):
        age = int(input("How old are you? "))
        if age < 18:
            print("You are too young")
            exit()
        else:
            print(f"Let's go, {firstname}!")
        return age

    def question_get():
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(["+", "-", "*", "/"])
        question = f"What is {num1} {operation} {num2}?"
        answer = eval(f"{num1} {operation} {num2}")
        return question, answer

    points = 0
    questions = [question_get() for _ in range(100)]

    for i, (question, correct_answer) in enumerate(questions, 1):
        print(f"Question {i}: {question}")
        user_answer = float(input("Enter the result: "))

        if round(correct_answer, 1) == round(user_answer, 1):
            print(f"Correct!")
            points += 1
        else:
            print(
                f"Incorrect. The correct answer was {correct_answer}, you get {points} points.")
            return
        print(f"Points: {points}")

    print(f"You scored {points} out of 100.")

    welcome()
    firstname = get_name()


main()
