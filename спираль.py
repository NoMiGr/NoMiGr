
n, m = map(int, input().split())

matrix = []
counter = 1

matrix = [[0] * m for _ in range(n)]

start_num= 0 # конец верхняя строка
i=1          # старт правая вертикаль
j=m-2         # старт нижняя строка
k=n-2         # старт левая вертикаль
num=1         # старт верхняя строка-1
i1=2          # старт правая вертикаль-1
j1=m-3        # старт нижняя строка +1
k1=n-3        # старт левая вертикаль +1
num1=2        # старт верхняя строка -2
i2=3          # старт правая вертикаль-2
j2=m-4        # старт нижняя строка +2
k2=n-4         # старт левая вертикаль +2
num2=3        # старт верхняя строка -3
i3=4          # старт правая вертикаль-3
j3=m-5        # старт нижняя строка +3
k3=n-5         # старт левая вертикаль +3
while  start_num < m:
    matrix[0][start_num] = start_num+1    # верхняя строка
    start_num += 1

if n >1 :
    while i < n:
        matrix[i][m-1] = start_num+1  # правая вертикаль
        start_num += 1
        i=i+1
if n > 1 and m>1:
    while j >=0:
        matrix[n-1][j] = start_num +1  # нижняя строка
        start_num += 1
        j=j-1

    while k > 0:
        matrix[k][0] = start_num + 1   # левая вертикаль
        start_num += 1
        k = k - 1
if n>2:
    while num < m-1:
        matrix[1][num] = start_num +1  # верхняя строка-1
        start_num += 1
        num=num+1
if m>2:
    while i1 < n - 1:
        matrix[i1][m - 2] = start_num+1   # правая вертикаль-1
        start_num += 1
        i1 = i1 + 1
if n>3:
    while j1 >= 1:
        matrix[n - 2][j1] = start_num +1   # нижняя строка +1
        start_num += 1
        j1 = j1 - 1
if m>3:
    while k1 > 1:
        matrix[k1][1] = start_num +1  # левая вертикаль +1
        start_num += 1
        k1 = k1 - 1
if n >4:
    while num1 < m - 2:
        matrix[2][num1] = start_num +1  # верхняя строка -2
        start_num += 1
        num1 = num1 + 1
if m>4:
    while i2 < n - 2:
        matrix[i2][m - 3] = start_num +1 # правая вертикаль-2
        start_num += 1
        i2 = i2 + 1
if n>5:
    while j2 >= 2:
        matrix[n - 3][j2] = start_num  +1  # нижняя строка +2
        start_num += 1
        j2 = j2 - 1
if m>5:
    while k2 > 2:
        matrix[k2][2] = start_num +1  # левая вертикаль +2
        start_num += 1
        k2 = k2 - 1
if n >6:
    while num2 < m - 3:
        matrix[3][num2] = start_num +1  # верхняя строка -3
        start_num += 1
        num2 = num2 + 1
if m>6:
    while i3 < n - 3:
        matrix[i3][m - 4] = start_num +1 # правая вертикаль-3
        start_num += 1
        i3 = i3 + 1
if n>7:
    while j3 >= 3:
        matrix[n - 4][j3] = start_num  +1  # нижняя строка +3
        start_num += 1
        j3 = j3 - 1
if m>7:
    while k3 > 3:
        matrix[k3][3] = start_num +1  # левая вертикаль +3
        start_num += 1
        k3 = k3 - 1


for row in matrix:
    for num in row:
        print(str(num).ljust(3), end='')
    print()



