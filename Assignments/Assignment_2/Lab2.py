print("**** Welcome to the LAB grade calculator ****")

name = input('Who are we calculating grades for?: ')

labs = int(input('Enter the Labs grade:'))

exams = int(input('Enter the Exams grade:'))

attendance = int(input('Enter the Attendance grade:'))

score = (labs * 0.7) + (exams * 0.2) + (attendance * 0.1)

print('The weighted grade for', name, 'is', score)

score = (labs * 0.7) + (exams * 0.2) + (attendance * 0.1)
if score >= 90:
    print(name, 'Has a letter grade of A')
elif score >= 80:
    print(name, 'Has a letter grade of B')
elif score >= 70:
    print(name, 'Has a letter grade of C')
elif score >= 60:
    print(name, 'Has a letter grade of D')
elif score < 60:
    print(name, 'Has a letter grade of F')

print("**** Thanks for using the Lab grade calculator ****")


