Colorful Flowers Count

#Your code below
x=int(input());l=input().split();l1=list(map(int,input().split()));a=int(input());r,b,g=0,0,0;te=0
for k in range(a):
    for h in range(x):
        if l[h]=='R' and l1[h]>0:r+=1;l1[h]-=1
        if l[h]=='G' and l1[h]>0 and (k+1)%2==0:g+=1;l1[h]-=1
        if l[h]=='B' and l1[h]>0 and (k+1)%3==0:b+=1;l1[h]-=1
print(r,g,b)