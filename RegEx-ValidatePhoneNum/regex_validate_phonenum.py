import re

for i in range(int(input("Enter num phone numbers: "))):
     if re.search(r'(^[789][0-9]{9})$', input("Enter phone number[{}]: " .format(i))):
        print("YES")
     else:
        print("NO")
   
