NEXT EQID FACTOR

#Your code below
x=int(input())
for k in range(x+1):
    c=str(x-k);d=str(x+k)
    if int(c)%int(str(c)[0]+str(c)[-1])==0:print(c);quit()
    if int(d)%int(str(d)[0]+str(d)[-1])==0:print(d);quit()