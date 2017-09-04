import re
l = re.split(',|\.', input("Enter Input String: "))
for i in l:
    if i:
        print(i)
