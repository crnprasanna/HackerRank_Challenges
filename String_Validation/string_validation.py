def chkStr(s, cmd):
    for i in s:
        if eval(cmd):
            return True
    return False
     
if __name__ == '__main__':
    s = input('Enter String of any type: ')
    print("Contains AlphaNumeric: {}" .format(chkStr(s,'i.isalnum()')))
    print("Contains Alpha: {}" .format(chkStr(s,'i.isalpha()')))
    print("Contains Digit: {}" .format(chkStr(s,'i.isdigit()')))
    print("Contains Lower: {}" .format(chkStr(s,'i.islower()')))
    print("Contains Upper: {}" .format(chkStr(s,'i.isupper()')))


