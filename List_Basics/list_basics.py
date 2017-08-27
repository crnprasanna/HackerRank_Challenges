if __name__ == '__main__':
    N = int(input("Enter number of commands you wish to enter (for list of commands, refer Readme.txt: "))
    if N < 1:
        print("Error in Input\n")
    l = []
    l_cmd = ['insert', 'print', 'remove', 'append', 'sort', 'pop', 'reverse']
    for i in range(N):
        cmd = input("Enter the Command-{}: " .format(i)).split()
        
        if l_cmd[0] in cmd:
            l.insert(int(cmd[1]), int(cmd[2]))
        elif l_cmd[1] in cmd:
            print(l)
        elif l_cmd[2] in cmd:
            l.remove(int(cmd[1]))
        elif l_cmd[3] in cmd:
            l.append(int(cmd[1]))
        elif l_cmd[4] in cmd:
            l.sort()
        elif l_cmd[5] in cmd:
            l.pop()
        elif l_cmd[6] in cmd:
            l.reverse()
        else:
            print("Invalid Input Cmd {} supported commands : {}" .format(cmd, l_cmd))

            
