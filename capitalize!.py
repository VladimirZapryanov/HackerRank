def solve(s):
    full_name = list(s)
    current_l = ' '
    for e in range(len(full_name)):
        if current_l == ' ' and full_name[e].islower:
            full_name[e] = full_name[e].upper()
        current_l = full_name[e]

    return ''.join(full_name)


s = input()
result = solve(s)

print(result)