'''
2)

file1 = 'orders_23072024.txt'

fildt = file1[]

print("filedate is ",fildt)

output 
------

file date is 23072024
file suffix is txt 
file prefix is orders 

note : derive file suffix using negative index
'''
file='orders_23072024.txt'
file1=file[-12:-4]
file2=file[-3:]
file3=file[0:6]
print('file date is ',file1)
print('file suffix is ',file2)
print('file prefix is ',file3)
