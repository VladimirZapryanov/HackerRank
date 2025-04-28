def average(array):
    unique_number = set(array)
    arr_n = sum(unique_number) / len(unique_number)
    return f'{arr_n:.3f}'


n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)
