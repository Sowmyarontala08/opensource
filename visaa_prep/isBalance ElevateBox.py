m=int(input())
n=list(map(int,input().split()))
o=sum(n)
p=0
q=[]
for i in range(m):
    r=o-p-n[i]
    balance=abs(p-r)
    q.append(balance)
    p+=n[i]
print(" ".join(map(str,q)))
