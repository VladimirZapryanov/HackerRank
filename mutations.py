def mutate_string(string, position, character):
    # string = list(string)
    # string[position] = character
    # string = ''.join(string)

    string = string[:position] + character + string[position+1:]

    return string


s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)
