from re import findall
r,c=map(int,input().split())
l=[[0 for j in range(c)] for i in range(r)]
q=int(input())
for i in input().split():
    n=[int(j) for j in findall('[0-9]+',i)]
    m=[j for j in findall('[rc]',i)]
    if len(n)==1:
        x,y=n[0],m[0]
        if y=='r':
            for k in range(c):
                l[x-1][k]+=1
        else:
            for k in range(r):
                l[k][x-1]+=1
    elif m[0]=='r':
        l[n[0]-1][n[1]-1]+=1
    else:
        l[n[1]-1][n[0]-1]+=1
for i in l:
    print(*i)