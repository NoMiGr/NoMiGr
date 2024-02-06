



n = int(input())
matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

max_element = -1e10 # A small negative number; change depending on your data range.
if n ==2:
    for i in range(n):
        for j in range(n):
            if max_element <= matrix[i][j]:
                max_element = matrix[i][j]

if n ==3:
    matrix[0][1]=-1e10
    matrix[2][1]=-1e10
    for i in range(n):
        for j in range(n):
            if max_element <= matrix[i][j]:
                max_element = matrix[i][j]
if n ==4:
    matrix[0][1]=-1e10
    matrix[0][2]=-1e10
    matrix[3][1]=-1e10
    matrix[3][2]=-1e10
    for i in range(n):
        for j in range(n):
            if max_element <= matrix[i][j]:
                max_element = matrix[i][j]

if n ==5:
    matrix[0][1]=-1e10
    matrix[0][2]=-1e10
    matrix[0][3] = -1e10
    matrix[1][2] = -1e10
    matrix[4][1]=-1e10
    matrix[4][2]=-1e10
    matrix[4][3] = -1e10
    matrix[3][2] = -1e10
    for i in range(n):
        for j in range(n):
            if max_element <= matrix[i][j]:
                max_element = matrix[i][j]

if n == 6:
    matrix[0][1] = -1e10
    matrix[0][2] = -1e10
    matrix[0][3] = -1e10
    matrix[0][4] = -1e10
    matrix[1][2] = -1e10
    matrix[1][3] = -1e10
    matrix[5][1] = -1e10
    matrix[5][2] = -1e10
    matrix[5][3] = -1e10
    matrix[5][4] = -1e10
    matrix[4][2] = -1e10
    matrix[4][3] = -1e10
    for i in range(n):
        for j in range(n):
            if max_element <= matrix[i][j]:
                max_element = matrix[i][j]
print(max_element)
# for i in range(n):

