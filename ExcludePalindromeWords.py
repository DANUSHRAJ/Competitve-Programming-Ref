S=list(map(str,input().strip().split()))
for i in S:
    if(i.lower()!=i[::-1].lower()):
        print(i,end=" ")
