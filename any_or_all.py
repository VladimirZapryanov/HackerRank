n = int(input())
numbers = [int(n) for n in input().split(' ')]

palindromic = False
all_positive = True
for n in numbers:
    if n < 0:
        all_positive = False
        break
    if str(n) == str(n)[::-1]:
        palindromic = True

condition = False
if all_positive and palindromic:
    condition = True

print(condition)


