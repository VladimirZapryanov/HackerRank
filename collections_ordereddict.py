from collections import OrderedDict

number_of_items = int(input())

items_dict = OrderedDict()
for _ in range(number_of_items):
    item_and_price = input().split()
    price = int(item_and_price[-1])
    item_and_price.pop()
    item_name = ''
    for e in item_and_price:
        item_name += e + ' '
    item_name = item_name.strip()
    if item_name not in items_dict:
        items_dict[item_name] = price
    else:
        items_dict[item_name] += price

for k, v in items_dict.items():
    print(k, v)
