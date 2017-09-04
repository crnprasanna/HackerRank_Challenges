import re
n = int(input('Enter number of input lines: '))

for i in range(n):
    inp = input("Enter line[{}]: " .format(i))
    inp1 = re.sub(r'(?<= )(&{2})(?= )', 'and', inp)
    print(re.sub(r'(?<= )(\|{2})(?= )', 'or', inp1))


