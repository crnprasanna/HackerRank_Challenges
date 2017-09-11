import re
from functools import reduce

charToStr= lambda x,y:x+y

lst = []
inp = raw_input('Enter String: ')
tmp =re.search(r'(?=.*?([a-z]+).*?)',inp)
if tmp:
	lst.append(tmp.group(1))
 
tmp =re.search(r'(?=.*?([A-Z]+).*?)',inp)
if tmp:
	lst.append(tmp.group(1))

if lst:
    lst=map(sorted,lst)
    lst = reduce(charToStr, reduce(charToStr, lst))

tmp =re.search(r'(?=.*?(\d+).*?)',inp)
if tmp:
	num = tmp.group(1)
	nfiltered= filter(lambda x: (x%2), map(int, num))+filter(lambda x: not(x%2), map(int, num))
	if lst:
		lst += reduce(charToStr,map(str,nfiltered))
	else:
	    lst = reduce(charToStr,map(str,nfiltered))

print(lst)
