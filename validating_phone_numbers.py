number = int(input())
for n in range(number):
    phone_number = input()
    if phone_number.isdigit():
        if len(phone_number) == 10:
            if phone_number[0] == '7' or phone_number[0] == '8' or phone_number[0] == '9':
                print('YES')
            else:
                print('NO')
        else:
            print('NO')
    else:
        print('NO')


