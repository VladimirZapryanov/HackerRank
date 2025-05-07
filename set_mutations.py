number_of_elements_a = int(input())
list_of_elements_a = set([int(n) for n in input().split()])
number_of_elements_n = int(input())

for _ in range(number_of_elements_n):
    operation_name, new_set = input().split()
    list_of_elements_new_set = set([int(n) for n in input().split()])

    if operation_name == 'update':
        list_of_elements_a.update(list_of_elements_new_set)
    elif operation_name == 'intersection_update':
        list_of_elements_a.intersection_update(list_of_elements_new_set)
    elif operation_name == 'difference_update':
        list_of_elements_a.difference_update(list_of_elements_new_set)
    elif operation_name == 'symmetric_difference_update':
        list_of_elements_a.symmetric_difference_update(list_of_elements_new_set)

print(sum(list_of_elements_a))