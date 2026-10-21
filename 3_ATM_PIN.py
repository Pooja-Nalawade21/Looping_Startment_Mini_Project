pin = 1234
attempt = 1
while attempt <= 3:
    user_pin = int(input("Enter PIN : "))
    if user_pin == pin:
        print("Access Granted")
        print("Attempts Used :", attempt)       
    else:
        print("Wrong PIN")
        attempt =attempt + 1
if attempt > 3:
    print("Card Temporarily Locked")
    print("Attempts Used : 3")