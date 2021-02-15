S=input().strip()
a=list(set(S))
a.sort()
for i in a:
    print(i,end="")
