number = int(input())
students = {}

for x in range(number):
    name, *line = input().split()
    student_score = [float(n) for n in line]
    students[name] = student_score

query_name = input()
score_nums = len(students[query_name])
average_score = sum(students[query_name]) / score_nums
print(f'{average_score:.2f}')
