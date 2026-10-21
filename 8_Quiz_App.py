questions = [
    "What is the Capital of India? ",
    "How many days are there in a week? ",
    "What is 5 + 5? ",
    "Which planet do we live on? ",
    "What is the color of the sky? "
]

answers = [
    "delhi",
    "7",
    "10",
    "earth",
    "blue"
]

score = 0

for i in range(5):
    user_answer = input(questions[i]).lower()

    if user_answer == answers[i]:
        score += 1

percentage = (score / 5) * 100

print("\nScore =", score)
print("Percentage =", percentage)

if percentage >= 80:
    print("Excellent")

elif percentage >= 60:
    print("Good")

else:
    print("Keep Practicing")