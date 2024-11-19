N = int(input())
matrix =[]
for _ in range(N):
    row = list(map(int, input().split()))
    matrix.append(row)
transpose = [[matrix[j][i] for j in range(N)] for i in range(N)]
for row in transpose:
    print(" ".join(map(str, row)))
