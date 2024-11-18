def m(n,arr):
    return arr[1:]+arr[:1]
n=int(input())
arr=list(map(int,input().split()))
print(" ".join(map(str,m(n,arr))))
