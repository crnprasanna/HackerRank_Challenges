import re

instr = input("Enter Postal Code to be validated: ")
inp = int(instr)
ctr = -1
for mat in re.finditer(r'(?=(\d)\d\1)', instr):
    ctr += 1
    
print(not bool(ctr or inp < 100000 or inp > 999999))
