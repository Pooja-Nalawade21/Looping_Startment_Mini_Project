days = int(input("Enter Number of Days : "))
total = 0
count = 0
maximum = 0
for i in range(1, days + 1):
    units = int(input(f"Enter Units Consumed on Day {i} : "))
    total = total + units
    if units > 10:
        count += 1
    if units > maximum:
        maximum = units
average = total / days
print("\nTotal Units =", total)
print("Average Usage =", average)
print("High Usage Days =", count)
print("Maximum Daily Usage =", maximum)
if total > 300:
    print("High Usage")
else:
    print("Normal Usage")
