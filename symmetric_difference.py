int_m = int(input())
m_numbers = set([int(n) for n in input().split()])
int_n = int(input())
n_numbers = set([int(n) for n in input().split()])

sym_dif = m_numbers.symmetric_difference(n_numbers)
new_list = sorted(list(sym_dif))
for el in new_list:
    print(el)

