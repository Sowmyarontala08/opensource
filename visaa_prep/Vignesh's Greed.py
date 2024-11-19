N = int(input())
sticks = list(map(int, input().split()))
sticks.sort()
for i in range(N - 1, 1, -1):
    a, b, c = sticks[i - 2], sticks[i - 1], sticks[i]
    if a + b > c:
        print(a + b + c)
        break
else:
    print(-1)
