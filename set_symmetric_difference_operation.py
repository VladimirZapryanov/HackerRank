num_of_english_student = int(input())
students_number_english = [int(s)for s in input().split(' ')]
num_of_french_student = int(input())
students_number_french = [int(s)for s in input().split(' ')]

all_students = set(students_number_english).symmetric_difference(set(students_number_french))
print(len(all_students))