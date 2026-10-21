secret = 21
attempt = 1
while attempt <= 5:
    guess = int(input("Enter Your Guess : "))
    if guess == secret:
        print("You Won!")
        print("Attempts Used :", attempt)
    elif guess < secret:
        print("Too Low")
    else:
        print("Too High")
    attempt = attempt + 1
if attempt > 5:
    print("You Lost!")
    print("Secret Number Was :", secret)
    print("Attempts Used : 5")