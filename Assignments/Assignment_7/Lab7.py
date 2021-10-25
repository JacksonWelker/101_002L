mpg = int(input("Enter the minimum mpg: "))
if 0 < mpg > 100:
    print('ERROR, Number must be greater than 0, and less than 100.')

file = str(input("Enter the name of the input vehicle file:  "))

output = str(input("Enter the name of the file to output to:  "))

Enter the minimum mpg ==> bad input
You must enter a number for the fuel economy
Enter the minimum mpg ==> -10
Fuel economy given must be greater than 0
Enter the minimum mpg ==> 300F
uel economy must be less than 100
Enter the minimum mpg ==> 80

Enter the name of the input vehicle file ==> invalidfile.txt
Could not open file invalidfile.txt
Enter the name of the input vehicle file ==> vehicles2.txt

Enter the name of the file to output to ==> out*.txt
There is an IO Error out*.txt
Enter the name of the file to output to ==> output.txt

Could not convert value invalid for vehicle 1993 Chevrolet Caprice 
Could not convert value nine for vehicle 1993 Chrysler Concorde

