import re
pat = re.compile(r'(?<=[^aeiouAEIOU])[aeiouAEIOU]{2,}(?=[^aeiouAEIOU])')
exp = pat.findall(input("Enter String: "))

if exp:
    for wd in exp:
        print("Substring with 2 or more Vowels: {}\n" .format(wd))
else:
    print (-1)