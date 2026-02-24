'''program.py 
----------


s_id = input..
s_name = input..
sub1
sub2
sub3 
totalmarks = sub1 + sub2 +sbu3 

print("Totalmarks",totalmark)

res =[]



output
-----
Enter student id 
S1
Enter student name 
Ram
Enter sub1 marks 
90
Enter sub2 marks 
70
Enter sub3 marks 
50

TotalMarks : 210

*** STUDENT DETAILS *****

['S1','Ram',90,70,50,210]

----------
'''
s_id=input("Enter Student Id\n")
s_name=input('Enter Student Name\n')
sub1=input('Enter Subject 1 Marks\n')
sub2=input('Enter Subject 2 Marks\n')
totalmarks=int(sub1)+int(sub2)
print('Total marks is ',totalmarks)
res=[]
res.append(s_id)
res.append(s_name)
res.append(sub1)
res.append(sub2)
print('****Student Details****')
print(res)
