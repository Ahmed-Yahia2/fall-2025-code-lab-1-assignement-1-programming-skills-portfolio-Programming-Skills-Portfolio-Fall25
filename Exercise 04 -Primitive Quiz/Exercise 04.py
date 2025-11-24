quiz = {"What is the capital of France? ": "paris",
    "What is the capital of Germany? ": "berlin",
    "What is the capital of Italy? ": "rome",
    "What is the capital of Spain? ": "madrid",
    "What is the capital of Portugal? ": "lisbon",
    "What is the capital of Greece? ": "athens",
    "What is the capital of Austria? ": "vienna",
    "What is the capital of Belgium? ": "brussels",
    "What is the capital of Netherlands? ": "amsterdam",
    "What is the capital of Switzerland? ": "bern"}
score = 0
for question, correct_answer in quiz.items():
    answer = input(question)
    if answer.lower().strip() == correct_answer:
        print("Correct!")
        score = 1
    else:
        print("Wrong! The correct answer is:", correct_answer.capitalize())
        print("You got", score, "out of", len(quiz),"correct!")