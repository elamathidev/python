def grade(mark):
    if mark == 100:
        return 'O+'
    elif mark >= 90:
        return 'O'
    elif mark >= 80:
        return 'A+'
    elif mark >= 70:
        return 'A'
    elif mark >= 60:
        return 'B+'
    elif mark >= 50:
        return 'B'
    elif mark >= 40:
        return 'C+'
    elif mark >= 35:
        return 'C'
    else:
        return 'Fail'

mark = float(input("Enter the student's mark: "))
grade = grade(mark)
if 0 <= mark <= 100:
    print(f"Student Grade is: {grade}")
else:
    print("Invalid input, please enter between 0 to 100 or numberic values only")

