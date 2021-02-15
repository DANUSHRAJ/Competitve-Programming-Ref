S=input().strip()
count=0
for i in S:
    if S.count(i)>1:
        count+=1
if count==len(S):
    print("yes")
else:
    print("no")
