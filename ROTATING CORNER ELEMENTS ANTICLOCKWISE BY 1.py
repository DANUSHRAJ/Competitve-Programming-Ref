# ROTATING CORNER ELEMENTS ANTICLOCKWISE BY 1

#Your code below
x=int(input());l=[input().split() for _ in range(x)];m,n=0,1
for k in range(x//2):
    a=l[k][m];b=l[k][-n];c=l[x-k-1][m];d=l[x-k-1][-n]
    l[x-k-1][m],l[x-k-1][-n],l[k][-n],l[k][m]=a,c,d,b;m+=1;n+=1
for k in l:print(*k)
#print("DAN")