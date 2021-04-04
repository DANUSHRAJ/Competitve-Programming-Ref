FIND SUBMATRIX MISSING VERTICAL EDGES

DC->#Your code below
x,y=map(int,input().split());
l1=[input().split() for _ in range(x)];l2=[input().split() for _ in range(x)]
l3=[k for k in l1 if len(k)<y];l4=[k for k in l2 if len(k)<y];
l3=[list(k) for k in zip(*l3)];l4=[list(k) for k in zip(*l4)];
l5=[];l6=[]
for k in range(len(l3)):
    if l3[k]!=l4[k]:l5.append(l3[k]);l6.append(l4[k])
l7=l6+[l5[-1]]
for k in zip(*l7):print(*k)