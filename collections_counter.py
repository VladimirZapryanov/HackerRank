number_of_shoes = int(input())
shoes_size = [int(s) for s in input().split()]
number_of_customers = int(input())

total_money = 0
for x in range(number_of_customers):
    size, money = [int(n) for n in input().split()]
    if size in shoes_size:
        shoes_size.remove(size)
        total_money += money

print(total_money)
