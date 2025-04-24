student_list = []

for _ in range(int(input())):
    current_student = []
    name = input()
    score = float(input())
    current_student.append(name)
    current_student.append(score)
    student_list.append(current_student)

score_list = []
for s in student_list:
    s_name = s[0]
    s_score = s[1]
    score_list.append(s_score)
score_list = sorted(score_list)
second_score = list(set(score_list))[1]

second_score_students = []
for s in student_list:
    s_name = s[0]
    s_score = s[1]
    if s_score == second_score:
        second_score_students.append(s_name)

second_score_students = sorted(second_score_students)
for e in second_score_students:
    print(e)


