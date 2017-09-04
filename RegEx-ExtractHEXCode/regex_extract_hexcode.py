import re

for line in range(int(input("Enter number of lines to be validated: "))):
    for i in re.findall(r'.+?(#[a-fA-F0-9]{6}|#[a-fA-F0-9]{3})', input("Enter Line[{}]: " .format(line))):
        print(i)
