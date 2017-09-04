import re
mat = re.search(r'(?<=([a-zA-Z0-9]))(?=\1)',input("Enter Input String: "))
if mat:
    print(mat.groups()[0])
else:
    print('-1')
