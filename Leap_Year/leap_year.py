def is_leap(year):
    leap = "{} is not a Leap Year" .format(year)
    
    # Write your logic here
    if year < 1900 and year > pow(10,5):
        print("Enter year in range 1900 to 10**5\n")
    
    if (year%4 == 0) and (year%400 ==0 or year%100 != 0):
        leap = "{} is a Leap Year" .format(year)
            
    return leap
	
year = int(input("Enter Year to be checked: "))
print(is_leap(year))