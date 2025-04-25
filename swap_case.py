def swap_case(s):
    s = list(s)
    length_s = len(s)

    for e in range(length_s):
        if s[e].isupper():
            s[e] = s[e].lower()
        elif s[e].islower:
            s[e] = s[e].upper()

    return ''.join(s)


s = input()
result = swap_case(s)
print(result)
