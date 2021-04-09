#Your code below
import math as CNN
x,y=map(int,input().split());l=[list(map(int,input().split())) for _ in range(x)];a,b=map(int,input().split());l1=[list(map(int,input().split())) for _ in range(a)]
mr=min(x,a);mc=min(y,b)
for k in range(mr):
    for h in range(mc):
        print(CNN.gcd(l[k][h],l1[k][h]),end=' ')
    print()
#print('DAN')