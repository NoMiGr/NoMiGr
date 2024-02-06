



# n = int(input())
# matrix = []
# reverse_diag = []
# new_matrix = []
#
# # заполняем матрицу
# for _ in range(n):
#     row = list(map(int, input().split()))
#     matrix.append(row)
#
# # записываем элементы диагоналей сверху вниз
# for i in range(n):
#     reverse_diag.append(matrix[i][i])
#
# # меняем элементы диагоналей наоборот снизу вверх
# reverse_diag.reverse()
#
# # меняем местами диагонали
# for i in range(n):
#     row = []
#     for j in range(n):
#         if i == j:
#             row.append(reverse_diag[i])
#         elif i == n - 1 - j:
#             row.append(reverse_diag[j])
#         else:
#             row.append(matrix[i][j])
#     new_matrix.append(row)
#
# # выводим полученную матрицу
# for row in new_matrix:
#     print(*row)

n = int(input())
matrix = []
reverse_diag = []
reverse_diag1 = []
new_matrix = []

# заполняем матрицу
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# записываем элементы диагоналей сверху вниз
for i in range(n):
    reverse_diag.append(matrix[i][i])
    reverse_diag1.append(matrix[i][n - 1 - i])

# меняем элементы диагоналей наоборот
# меняем элементы диагоналей наоборот
reverse_diag = reverse_diag[::-1]
reverse_diag1 = reverse_diag1[::-1]

# меняем местами диагонали
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(reverse_diag1[i])
        elif i == n - 1 - j:
            row.append(reverse_diag[i])
        else:
            row.append(matrix[i][j])
    new_matrix.append(row)

# выводим полученную матрицу
for row in new_matrix:
    print(*row)