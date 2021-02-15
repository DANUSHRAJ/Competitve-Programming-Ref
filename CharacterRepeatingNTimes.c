N=list(map(str,input().strip().split(" ")))
A=N[0]
B=int(N[1])
C=[]
for i in range(0,len(A)):
    if A.count(A[i])==B and A[i] not in C:
        C.append(A[i])
for i in C:
    print(i,end="")
