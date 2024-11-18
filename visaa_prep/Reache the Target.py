T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    runs_needed = X - Y + 1
    print(runs_needed)
