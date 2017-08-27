if __name__ == '__main__':
    x = int(input("Enter value for integer X: "))
    y = int(input("Enter value for integer Y: "))
    z = int(input("Enter value for integer Z: "))
    n = int(input("Enter value for integer N: "))
    print([ [i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n])