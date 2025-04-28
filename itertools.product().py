list_a = [int(e) for e in input().split(' ')]
list_b = [int(e) for e in input().split(' ')]
result = []

for a in list_a:
    for b in list_b:
        t = (a, b)
        result.append(t)

for i in result:
    print(i, end=' ')

