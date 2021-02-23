Split Integers & Sum

SOLUTION:

#Your code below
x=int(input());l=list(map(int,input().split()));z=int(input());c='';co=0;su=0
for k in range(x):
    if co+len(str(l[k]))<=z:
        co+=len(str(l[k]));print(l[k],end=' ');su+=l[k]
    else:print(su,l[k],sep='\n',end=' ');co=len(str(l[k]));su=l[k];
print(su)