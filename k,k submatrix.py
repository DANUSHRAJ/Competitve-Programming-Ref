#Your code below
x,y=map(int,input().split());l=[input().split() for _ in range(x)];l1=[]
for k in range(0,x,3):
    for h in range(0,y,3):
        l1.append([l[k][h:h+3],l[k+1][h:h+3],l[k+2][h:h+3]])