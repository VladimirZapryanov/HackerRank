def split_and_join(string):
    result = string.split(' ')
    result = '-'.join(result)
    return result


string = input()
final_string = split_and_join(string)
print(final_string)