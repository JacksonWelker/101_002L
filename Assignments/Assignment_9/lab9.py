def CrimeDataSolution():
    pass
    while True:
       try:
        i = input('Enter the name of the crime data file')
        i = open(i)
     except IOError:
        print("Could not find the file specified. not exists, not found")
    finally:
        pass.close
    
    
    with open(i, "r") as f:
        lines = f.readlines()
    
    print('The month with the highest # of crimes is', Reported_Date, 'with', sum.Offense)
    print('The offense with the highest # of of crimes is', Offense,'with', sum.offense,'offenses')
    
        pass2
    while True:
       try:
        x = input('Enter an offense')
        x = open(i)
     except IOError:
        print("Not a valid offense found, please try again")
    finally:
        pass2.close
        
    with open(x, "r") as f:
        lines = f.readlines()
    
    print('Arson offenses by sip code', Zip Code, '#', arson.offenses)
  