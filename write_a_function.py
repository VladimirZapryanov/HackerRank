def is_leap(year):
    leap = False
    if year % 100 == 0:
        if year % 4 == 0 and year % 400 == 0:
            leap = True
        else:
            leap = False
    elif year % 4 == 0 or year % 400 == 0:
        leap = True
    return leap


year = int(input())
print(is_leap(year))