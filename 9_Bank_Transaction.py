balance = float(input("Enter Opening Balance : "))
num = int(input("Enter Number of Transactions : "))

deposit_count = 0
withdraw_count = 0
rejected_count = 0

for i in range(1, num + 1):
    ttype = input("Enter Transaction Type (deposit/withdraw) : ").lower()
    amount = float(input("Enter Amount : "))

    if ttype == "deposit":
        balance = balance + amount
        deposit_count += 1
        print("Deposit Successful")

    elif ttype == "withdraw":
        if amount <= balance:
            balance = balance - amount
            withdraw_count += 1
            print("Withdrawal Successful")
        else:
            rejected_count += 1
            print("Insufficient Balance")

print("\nFinal Balance =", balance)
print("Deposit Count =", deposit_count)
print("Successful Withdrawal Count =", withdraw_count)
print("Rejected Withdrawal Count =", rejected_count)

if balance < 1000:
    print("Warning: Low Balance")