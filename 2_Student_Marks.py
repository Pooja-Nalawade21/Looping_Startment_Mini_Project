num=int(input("Enter the Number of students : "))
total=0
pass_count=0
fail_count=0
for i in range(1,num+1):
    name=input(f"Enter the Name of Student {i} : ")
    marks=int(input(f"Enter the marks of Student {i} out of 100 : "))
    if marks < 0 or marks > 100:
        print("Invalid Marks")
        continue
    total=total+marks
    if marks>=75:
        print("Congratulations!!You got A Grade.")
        pass_count=pass_count+1
    elif marks>=60:
        print("Congratulations!!You got B Grade.")
        pass_count=pass_count+1
    elif marks>=50:
        print("Congratulations!!You got C Grade.")
        pass_count=pass_count+1
    elif marks>=40:
        print("Congratulations!!You got D Grade.")
        pass_count=pass_count+1
    else:
        print("You're Fail.")
        fail_count=fail_count+1
average=total/num
print("-----------------Student Marks and Grade Report----------------------")
print("Class Average : ",average)
print("Pass Count : ",pass_count)
print("Fail Count : ",fail_count)