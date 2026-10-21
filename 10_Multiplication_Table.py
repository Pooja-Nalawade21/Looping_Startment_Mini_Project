num = int(input("Enter a Number for Table : "))

print("\nMultiplication Table")

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

start = int(input("\nEnter Start Number : "))
end = int(input("Enter End Number : "))

if start > end:
    print("Invalid Range")

else:
    even = 0
    odd = 0
    total = 0

    for i in range(start, end + 1):
        total = total + i

        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    print("\nEven Count =", even)
    print("Odd Count =", odd)
    print("Sum of Range =", total)