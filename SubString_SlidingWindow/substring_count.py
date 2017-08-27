def count_substring(string, sub_string):
    ctr = 0
    while string.count(sub_string):
        ctr += 1
        string = string[string.index(sub_string)+1:]
    return ctr

if __name__ == '__main__':
    string = input('Enter String').strip()
    sub_string = input('Enter SubString to count').strip()
    
    count = count_substring(string, sub_string)
    print(count)
