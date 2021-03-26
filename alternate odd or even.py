#Your code below
x=input().strip();al='';ab='';m,p,q=0,0,0
for k in range(len(x)):
    s=1
    for h in range(k,len(x)-1):
        if (int(x[h])%2==0 and int(x[h+1])%2==0) or (int(x[h])%2==1 and int(x[h+1])%2==1):
            break
        else:s+=1
    if s>m:
        m=s;p=k;q=k+s
print(x[p:q],'DAN')