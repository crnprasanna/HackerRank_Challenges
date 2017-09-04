import re

for i in range(int(input('Enter num card numbers to be validated: '))):
    inp = input('Enter Card Number [{}] : ' .format(i))
    inp1 = re.sub('-', '', inp)
    if len(re.findall(r'(?=^[4-6][\d]{3}-?[\d]{4}-?[\d]{4}-?[\d]{4}$)', inp)) and not len(re.findall(r'([\d])\1{3}', inp1)) :
           print("Valid")
    else:
           print("Invalid")
