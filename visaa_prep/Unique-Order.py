def m(n,arr):
    p,q=set(),[]
    for x in arr:
        if x not in p:
            q.append(x)
            p.add(x)
    return q
n=int(input())
arr=list(map(int,input().split()))
print(" ".join(map(str,m(n,arr))))
