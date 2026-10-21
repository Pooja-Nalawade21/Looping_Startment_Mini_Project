days=int(input("Enter the Number of Days : "))
total=0
highest=0
for i in range(1,days+1):
    exp=int(input(f"Enter the Expence of Day {i} : "))
    total=total+exp
    if exp>highest:
        highest=exp
avg=total/days
print("Total Expense : ",total)
print("Average Daily Expense : ",avg)
print("Highest Daily Expense : ",highest)
if total>5000:
    print("Budjet Alert...")
