string = input()
sub_string = input()

count = 0
current_string = ''
for i in range(len(string)):
    current_string += string[i]
    if len(current_string) > len(sub_string):
        current_string = current_string[1:]
    if current_string == sub_string:
        count += 1

print(count)