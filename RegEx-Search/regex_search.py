import re
for i in range(int(input())):
    print(bool(re.search(r'^[+-]{0,1}\d*\.\d+$', (input()))))
    

