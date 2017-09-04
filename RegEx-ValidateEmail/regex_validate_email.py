import re

for inp in range(int(input("Enter number of email id's to be validated: "))):
    str = input("Enter email ID [{}] : " .format(inp))
    if re.search(r'([a-zA-Z]+) <([a-zA-Z][\w\-.]+)@([a-zA-Z]+)\.([a-zA-Z]{1,3})>', str):
        print(str)
