N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
row_sum = [0] * N
col_sum = [0] * N
for i in range(N):
    for j in range(N):
        row_sum[i] += matrix[i][j]
        col_sum[j] += matrix[i][j]
result = []
for i in range(N):
    result.append(row_sum[i] + col_sum[i])
print(' '.join(map(str, result)))
