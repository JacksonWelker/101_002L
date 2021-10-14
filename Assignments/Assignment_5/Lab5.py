

def get_school():
    if school(:4) == 1:
        print("School of Computing and Engineering")
    elif school(:4) == 2:
        print("School of Law")
    elif school(:4) == 3:
        print("College of Arts and Sciences")
    else:
        print("Invalid School")


def get_grade():
    if school(:5) == 1:
        print("Freshman")
    elif school(:5) == 2:
        print("Sophomore")
    elif school(:5) == 3:
        print("Junior")
    elif school(:5) == 4:
        print("Senior")
    else:
        print("Invalid Grade")

def character_value():
    if school == 'a':
        print('0')
    elif school == 'b':
        print('1')
    else:
        print('25')

def get_check_digit():
    if school == 'a':
        print('0')
    elif school == 'b':
        print('1')
    else:
        print('25')

def verify_check_digit():
    if len(school) != 10:
        print('False, "The length of the number given must be 10"')
    elif school(0:4) != [A-Z]:
        print('False, "The first 5 characters must be A-Z, the invalid character is at 3is %"')
    elif school(6:8) != [0-9]:
        print('False, "The last 3 characters must be 0-9, the invalid character is at 7 is X"')
    elif school(:4) != ('1','2','3'):
        print('False, "The sixth character must be a 1, 2, or 3"')
    elif school(:5) != ('1','2','3','4'):
        print('False, "The seventh caracter must be a 1, 2, 3, or 4"')
    elif school != get_check_digit:
        print('False, "Check digit 8 does not math calculated value 2:')
    else:
        print('True')

print('Linda Hall')
print('Library Card Check')
print('==================================')


school = str(input("Input library card: "))


Linda Hall
Libary Card Check
============================================================

Enter Libary Card. Hit enter to exit ===> XXY92
Library card is invalid.
The length of the number given must be 10

Enter Libary Card. Hit enter to exit ===> 1111111111
Library Card is invalid
The first 5 characteristics must be A-Z, the invalid character  at 0 is 1

Enter Libary Card. Hit enter to exit ===> VWXYZ34592
Library Card is valid
The card belings to a student in College of Arts and Sciences
The card belongs to a Senior

Enter Libary Card. Hit enter to exit ===> BINGH14592
Libary card is invalid.
Check digit 2 does not malth calcualted value 0.and

Enter Libary Card. Hit enter to exit ===> BINGH14590
Library Card is valid.
The card belings to a student in School of Computing and Engineering SEC
The card belongs to a Senior


