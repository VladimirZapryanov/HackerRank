s = input()

has_alphanumeric = False
for l in s:
    if l.isalnum():
        has_alphanumeric = True
print(has_alphanumeric)

has_alphabetical = False
for l in s:
    if l.isalpha():
        has_alphabetical = True
print(has_alphabetical)

has_digit = False
for l in s:
    if l.isdigit():
        has_digit = True
print(has_digit)

has_lowercase = False
for l in s:
    if l.islower():
        has_lowercase = True
print(has_lowercase)

has_uppercase = False
for l in s:
    if l.isupper():
        has_uppercase = True
print(has_uppercase)
