

n = input()

is_same = True

for i in range(len(n)-1):
    if n[i] != n[i+1]:
        is_same = False
        break

if is_same:
    print('YES')
else:
    print('NO')



