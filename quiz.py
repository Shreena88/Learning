print("quiz started")

score = 0
questions_options_answers = {
    "What is the capital of France?": {
        "options": ["A) Paris", "B) London", "C) Rome", "D) Berlin"],
        "answer": "A"
    },
    "What is the largest planet in our solar system?": {
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "C"
    },
    "Who wrote 'To Kill a Mockingbird'?": {
        "options": ["A) Harper Lee", "B) Mark Twain", "C) J.K. Rowling", "D) Ernest Hemingway"],
        "answer": "A"
    },
    "What is the chemical symbol for water?": {
        "options": ["A) H2O", "B) CO2", "C) O2", "D) NaCl"],
        "answer": "A"
    },
    "What is the largest mammal?": {
        "options": ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Hippopotamus"],
        "answer": "B"
    }
}   

for question, data in questions_options_answers.items():
    print(question)
    for option in data["options"]:
        print(option)
    user_answer = input("Enter your answer (A, B, C, or D): ").upper()
    if user_answer == data["answer"]:
           score += 1
    else:
        print("Wrong answer!")

print(f"Your final score is: {score}/{len(questions_options_answers)}")
