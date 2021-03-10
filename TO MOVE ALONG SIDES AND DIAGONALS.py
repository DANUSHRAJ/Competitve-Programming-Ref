r,c=map(int,input().split())
l=[input().split() for i in range(r)]
for i in range(r):
    for j in range(c):
        if l[i][j]=='+':
            if i>0 and l[i-1][j] not in '+x':
                l[i-1][j]='*'
            if j>0 and l[i][j-1] not in '+x':
                l[i][j-1]='*'
            if i+1<r and l[i+1][j] not in '+x':
                l[i+1][j]='*'
            if j+1<c and l[i][j+1] not in '+x':
                l[i][j+1]='*'
        elif l[i][j]=='x':
            if i>0 and j>0 and l[i-1][j-1] not in '+x':
                l[i-1][j-1]='*'
            if i>0 and j+1<c and l[i-1][j+1] not in '+x':
                l[i-1][j+1]='*'
            if j>0 and i+1<r and l[i+1][j-1] not in '+x':
                l[i+1][j-1]='*'
            if i+1<r and j+1<c and l[i+1][j+1] not in '+x':
                l[i+1][j+1]='*'
print(sum([i.count('P') for i in l]))