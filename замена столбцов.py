


n= int(input())
m= int(input())

matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

i, j = map(int, input().split())

for k in range(n):
    matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i]

for row in matrix:
    print(' '.join(map(str, row)))


