def wrap(string, max_width):
    count = 0
    current_text = ''
    for l in string:
        current_text += l
        count += 1
        if count == max_width:
            count = 0
            current_text += '\n'

    return current_text


string = input()
max_width = int(input())

print(wrap(string, max_width))
