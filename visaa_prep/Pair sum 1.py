N = int(input())
arr = list(map(int, input().split()))
k = int(input())
visited = set()
found = False
for num in arr:
    complement = k - num
    if complement in visited:
        found = True
        break
    visited.add(num)
if found:
    print("true")
else:
    print("false")
