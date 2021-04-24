n=int(input())
l=list(map(int,input().split()))
arr=[]
c=[l[0]]
for x in l[1:]:
    if abs(c[-1]-x)==1:
        c.append(x)
    else:
        arr.append(c)
        c=[x]
if c:
    arr.append(c)
for x in arr:
    a=min(x)
    b=max(x)
    print(str(a)+'-'+str(b),end=" ")
