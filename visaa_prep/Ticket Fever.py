T = int(input())
results = []
for _ in range(T):
    N, M = map(int, input().split())
    results.append(max(0, N - M))
for result in results:
    print(result)
