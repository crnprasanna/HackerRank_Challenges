if __name__ == '__main__':
    n = int(input("Enter Number of Integers to be entered: "))
    l = list(map(int, input("Enter integer seperated by space: ").split()))
    lst = l[:]
    [l.remove(max(l)) for i in range(l.count(max(l))) ]
    
    if l:
	    print("Second Largest Max : {}\n" .format(max(l)))
    else:
	    print("No second largest number found in list - {}\n" .format(lst))
