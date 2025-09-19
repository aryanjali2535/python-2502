# Student Grade Tracker
# collecting information from student
student_Id = int(input("Enter Student Id :"))
student_name = input("Enter student Name :")
student_attendance = int(input("Enter student attendance :"))
# Asking student to enter score/marks
asking_student = input("Do you want to enter the score(yes/no) ? :")
total = 0
count = 0
if asking_student == "yes":
    score = int(input("Enter score 1 :"))
    total += score
    count +=1
elif asking_student == "no":
    print("Ok")
else:
    print("Enter yes/no")
while True:
    another_score = input("Do you want to enter another score(yes/no) ? :")
    if another_score == "yes":
        score = int(input(f"Enter score {count +1} :"))
        total += score
        count += 1
    elif another_score == "no":
        print("ok thank you")
        break
    else:
        print("please enter only 'yes' or 'no'.")
#total calucation
print("Total scores entered :", count)
print("sum of all scores :", total)
#Average
if count >0:
    average = total/count
    print("Average score :", average)
else:
    print("no scores entered")
#grading system
if average >= 85:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"
print("Grade:",grade)
# Attendence
if student_attendance < 75:
    print("Warning: low attendance")
else:
    print("ok good attendance")
# Award eligibility check
if student_attendance >= 75 and grade == "A":
    print("good attendance and also have 'A' grade give award to student")
else:
    print("not eligible")






