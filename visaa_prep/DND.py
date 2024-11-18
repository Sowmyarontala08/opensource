def a(n,m,arr):
    p=0
    q=0
    for num in arr:
        if num%m==0:
            q+=num
        else:
            p+=num
    return  q-p
n,m=map(int,input().split())
arr=list(map(int,input().split()))
print(a(n,m,arr))
