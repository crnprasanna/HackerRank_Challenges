def mutate_string(string, position, character):
    return (string[:position]+character+string[position+1:])

if __name__ == '__main__':
    s = input("Enter String: ")
    i, c = input("Enter position to be replace and character to be replaced: ").split()
    s_new = mutate_string(s, int(i), c)
    print("Output String: {}\n" .format(s_new))