






m = int(input())
n = int(input())
math_students = set()
it_students = set()
duplicates_math = set()
duplicates_it = set()
for _ in range(m):
    student = input()
    if student in math_students:
        duplicates_math.add(student)
    else:
        math_students.add(student)

for _ in range(n):
    student = input()
    if student in it_students:
        duplicates_it.add(student)
    else:
        it_students.add(student)

math_students.difference_update(duplicates_math)
it_students.difference_update(duplicates_it)

math_only_students = math_students.difference(it_students)
it_only_students = it_students.difference(math_students)

if len(math_only_students) == 0 and len(it_only_students) == 0:
    print("NO")
else:
    print(len(math_only_students) + len(it_only_students))

