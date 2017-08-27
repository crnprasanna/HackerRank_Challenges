import textwrap as twrap
def merge_the_tools(string, k):
    # your code goes here
    buf = twrap.wrap(string, k)
    for wd in buf:
        lwd = list(wd)
        lwd.reverse()
        for i in range(len(lwd)):
            if lwd.count(lwd[i]) > 1:
                lwd.remove(lwd[i])
            if i >= len(lwd):
                 break
        print(str(lwd.reverse()))
       
            
            
if __name__ == '__main__':
    string, k = input('Enter Input string: '), int(input('Enter split size: '))
    merge_the_tools(string, k)
