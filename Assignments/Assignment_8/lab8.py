print('Grade Menu')
print('1 - Add Test')
print('2 - Remove Test')
print('3 - Clear Tests')
print('4- Add Assignment')
print('5 - Remove Assignment')
print('6 - Clear Assignments')
print('D - Display Scores')
print('Q - Quit')

testlst = []
assignlst = []

avgtestlst= sum(testlst)/len(testlst)
avgassignlst = sum(assignlst)/len(assignlst)

weighted = (avgassignlst * 0.4) + (avgassignlst * 0.6)

mintest = min(avgtestlst)
minassign = min(avgassignlst)

maxtest = max(avgtestlst)
maxassign = max(avgassignlst)

menu = input(':')

if menu == 1:
    ntest = input('Enter the new test score 0-100: ')
    tesstlst.append(ntest)
elif menu == 2:
    rtest = input('Enter a test to remove: ')
    testlst.remove(rtest)
elif menu == 3:
    testlst.clear
elif menu == 4:
    nassign = input('Enter the new Assignment score 0-100: ')
    assignlst.append(nassign)
elif menu == 5:
    rassign = input('Enter a Assignment to remove:  ')
    assignlst.remove(rasssign)
elif menu == 6:
    assignlst.clear
elif menu == 7:
    print("The max of test is", maxtest)
    print("The minimum of test is", mintest)
    print("The verage of minimum is ", avgtestlst)
    print("The max of assignment is", maxassign)
    print("The minimum of assignment is", minassign)
    print("The average of assignent is", avgassignlst)
    print("The weighted total is", weighted)
else:
    exit()


Grade Menu
1 -Add Test
2 -Remove Test
3 -Clear Tests
4 -Add Assignment
5 -Remove Assignment
6 -Clear Assignments
D -Display Scores
Q -Quit

==> d
Type               #       min       max       avg       std
============================================================
Tests              0       n/a       n/a       n/a       n/a
Programs           0       n/a       n/a       n/a       n/a
The weighted scores is       0.00

Grade Menu
1 -Add Test
2 -Remove Test
3 -Clear Tests
4 -Add Assignment
5 -Remove Assignment
6 -Clear Assignments
D -Display Scores
Q -Quit

==> 1
Enter the new Test score 0-100 ==> 90

Grade Menu
1 -Add Test
2 -Remove Test
3 -Clear Tests
4 -Add Assignment
5 -Remove Assignment
6 -Clear Assignments
D -Display Scores
Q -Quit

==> 1
Enter the new Test score 0-100 ==> 95

Grade Menu
1 -Add Test
2 -Remove Test
3 -Clear Tests
4 -Add Assignment
5 -Remove Assignment
6 -Clear Assignments
D -Display Scores
Q -Quit

==> 4
Enter the new Assignment score 0-100 ==> 70

Grade Menu
1 -Add Test
2 -Remove Test
3 -Clear Tests
4 -Add Assignment
5 -Remove Assignment
6 -Clear Assignments
D -Display Scores
Q -Quit

==> 4
Enter the new Assignment score 0-100 ==> 82

Grade Menu
1 -Add Test
2 -Remove Test
3 -Clear Tests
4 -Add Assignment
5 -Remove Assignment
6 -Clear Assignments
D -Display Scores
Q -Quit

==> 4
Enter the new Assignment score 0-100 ==> 88

Grade Menu
1 -Add Test
2 -Remove Test
3 -Clear Tests
4 -Add Assignment
5 -Remove Assignment
6 -Clear Assignments
D -Display Scores
Q -Quit

==> 4
Enter the new Assignment score 0-100 ==> 103

Grade Menu
1 -Add Test
2 -Remove Test
3 -Clear Tests
4 -Add Assignment
5 -Remove Assignment
6 -Clear Assignments
D -Display Scores
Q -Quit

==> 5
Enter the Assignment to remove 0-100 ==> 100
Could not find that score to remove

Grade Menu
1 -Add Test
2 -Remove Test
3 -Clear Tests
4 -Add Assignment
5 -Remove Assignment
6 -Clear Assignments
D -Display Scores
Q -Quit

==> 5
Enter the Assignment to remove 0-100 ==> 103

Grade Menu
1 -Add Test
2 -Remove Test
3 -Clear Tests
4 -Add Assignment
5 -Remove Assignment
6 -Clear Assignments
D -Display Scores
Q -Quit

==> d
Type               #       min       max       avg       std============================================================
Tests              2      90.0      95.0     92.50      2.50
Programs           3      70.0      88.0     80.00      7.48
The weighted scores is      87.50

Grade Menu
1 -Add Test
2 -Remove Test
3 -Clear Tests
4 -Add Assignment
5 -Remove Assignment
6 -Clear Assignments
D -Display Scores
Q -Quit

==> q
>>>
    

    
