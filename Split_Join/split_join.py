def split_and_join(line):
    # write your code here
    return ("-".join(line.split()))
	
if __name__ == '__main__':
    line = input("Enter your string seperated by space: ")
    result = split_and_join(line)
    print("Output String: {}\n" .format(result))