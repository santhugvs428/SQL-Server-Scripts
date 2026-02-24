'''program.py 
---------
n  = int(input("Enter numbero fstudnets")) 

for i in range(n):
   std_id --> input 
   std-nm --> input
   sub1 ---> input 
   sub2  --> input 
   totalmark ---> sub1+sub2 
  
    printstatments

output 
------
Enter number of students 
2

Enter student id 
S1 
Enter student name 
krishna
Enter sub1 marks 
90
Enter sub2 marks 
80

STUDENT ID : S1 
STUDNET NAME : krishna 
TOTAL MARKS  : 170

Enter student id 
S2 
Enter student name 
ram
Enter sub1 marks 
70
Enter sub2 marks 
60

STUDENT ID : S2
STUDNET NAME : ram 
TOTAL MARKS  : 130
'''

n=int(input('Enter Number Of Students\n'))
for i in range(n):
    s_id=input('Enter Student ID\n')
    s_name=input('Enter Student Name\n')
    sub1=int(input('Enter Sub1 Marks\n'))
    sub2=int(input('Enter Sub2 Marks\n'))
    print('STUDENT ID:',s_id)
    print('STUDENT NAME:',s_name)
    print('TOTAL Marks:',sub1+sub2)
