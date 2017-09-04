import re

for i in range(int(input("Enter Number of UID's to be validated: "))):
    inp = input("Enter UID[{}]: " .format(i))
    if len(re.findall(r'(?=(\w)).+?\1', inp)):
        print("Invalid")
    elif len(re.findall(r'^(?=[a-zA-Z0-9]{10}$)', inp)) == 0:
        print("Invalid")
    elif len(re.findall(r'(?=\d\D*?\d\D*?\d)', inp)) == 0:
        print("Invalid")
    elif len(re.findall(r'(?=[A-Z][^A-Z]*?[A-Z])', inp)) == 0:
        print("Invalid")
    else:
        print("Valid")
