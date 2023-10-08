# Python Quiz game

questions = ("How many teeth in a Beluga whale mouth ",
            "Day on 1st january 2023",
            "3 spoons in a plate above your head:",
            "How much half kilo milk is in gm term ",
            "What comes after eating zinger Burger")

options = (("A.More than 40",
            "B. Search Google" ),
("A.Monday, Wednesday, Friday, Sunday",
            "B. Tuesday, Thursday, Saturday" ),
("A.PillBox hat",
            "B. Fan  "),
("A. 500 gram",
            "B. ((2 - 0.5) - 1/2 ) /2 = _l"),
("A. More Craving",
            "B. Diet") )

answers = ("B", "A", "B", "B", "A")
guesses = []
score = 0
question_num = 0

i = 0
for i in questions:
    print("--------------------------------")
    print(i)
    for i in options[question_num]:
        print(i)

    guess = input("Enter A or B :").upper()  # The upper() method returns a string where all characters are in upper case.
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print({answers[question_num]}, "is the correct answer") # Gotta check this step

    question_num += 1

print("--------------------------------")
print("          Results               ")
print("--------------------------------")

print("answers:", end=" ")
for i in answers:
    print(i, end=" ")
print()

print("guesses:", end=" ")
for i in guesses:
    print(i, end=" ")
print()

print(score)
score = int(score/ len(questions) * 100)
print(score)
print(f"Your score is: {score}%")


