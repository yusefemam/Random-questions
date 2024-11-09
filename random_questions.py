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

    def question_get(firstname):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(["+", "-", "*", "/"])
        question = f"What is {num1} {operation} {num2}?"
        answer = eval(f"{num1} {operation} {num2}")
        return question, answer

    welcome()  
    firstname = get_name()  
    age = get_age(firstname)  
    

    points = 0
    questions = [question_get(firstname) for _ in range(100)]  # Generate 100 questions

    for i, (question, correct_answer) in enumerate(questions, 1):
        print(f"Question {i}: {question}")
        user_answer = float(input("Enter the result: "))

        
        if round(correct_answer, 1) == round(user_answer, 1):
            print(f"Correct, Good job {firstname}!")
            points += 1
        else:
            print(
                f"Incorrect. The correct answer was {correct_answer}. You have {points} points, Try again {firstname}!.")
            break  
        print(f"Points: {points}")

    
    print(f"You scored {points} out of 100.")
    firstname = question_get(firstname)  


main()
