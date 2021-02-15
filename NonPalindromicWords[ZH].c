S=list(map(str,input().strip().split()))
flag=0
for i in S:
    if(i.lower()!=i[::-1].lower()):
        print(i,end=" ")
        flag=1
if flag==0:
    print("-1")
