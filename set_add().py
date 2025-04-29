n = int(input())
country_set = set()

for c in range(n):
    country = input()
    country_set.add(country)

print(len(country_set))