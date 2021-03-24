SOLUTION 1:

#Your code below
x,y,z=map(int,input().split())
l=[input().split() for _ in range(x)];co=0;tc=0
a,b,c=map(int,input().split())
if z<=a:
    for k in range(x):
        for h in range(a):
            co=0
            for m in range(h,a):
                if l[k][m]=='0':co+=1
                else:break
            if co>=z:tc+=1
if z<=b:
    for k in range(x):
        for h in range(a,a+b):
            co=0
            for m in range(h,a+b):
                if l[k][m]=='0':
                    co+=1
                else:break
            if co>=z:tc+=1
if z<=c:
    for k in range(x):
        for h in range(a+b,a+b+c):
            co=0
            for m in range(h,a+b+c):
                if l[k][m]=='0':co+=1
                else:break
            if co>=z:tc+=1
print(tc)

SOLUTION 2:

x,y,z=map(int,input().split())
l=[list(map(int,input().split())) for i in range(x)]
a,b,c=map(int,input().split())
k=[]
for i in l:
    k.append([i[:a],i[a:a+b],i[a+b:]])
n=0
for i in k:
    for j in i:
        for s in range(len(j)-z+1):
            if 1 not in j[s:s+z]:
                n+=1
print(n)