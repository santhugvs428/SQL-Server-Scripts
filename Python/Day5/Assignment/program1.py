'''program
----------

code = 'INDTGHYD500018'

c_code = code[0:3]
..
..

print("COUNTRY CODE :",c_code)

output 
------
COUNTRY CODE : IND 
STATE   CODE : TG 
CITY    CODE : HYD
pincode      : 5000018
'''
code='INDTGHYD500018'
code1=code[0:3]
code2=code[3:5]
code3=code[5:8]
code4=code[-6:]
print("country code :",code1)
print("state code :",code2)
print("city :",code3)
print("pincode :",code4)
