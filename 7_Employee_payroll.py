num = int(input("Enter Number of Employees : "))

total_payroll = 0

for i in range(1, num + 1):
    name = input(f"Enter Employee Name {i} : ")
    basic = float(input("Enter Basic Salary : "))
    overtime = int(input("Enter Overtime Hours : "))

    overtime_pay = overtime * 200

    gross = basic + overtime_pay

    if gross >= 50000:
        deduction = gross * 10 / 100
    else:
        deduction = gross * 5 / 100

    net = gross - deduction

    total_payroll = total_payroll + net

    print("\nEmployee Name :", name)
    print("Gross Salary :", gross)
    print("Deduction :", deduction)
    print("Net Salary :", net)

print("\nTotal Net Payroll :", total_payroll)
print("Employee Count :", num)