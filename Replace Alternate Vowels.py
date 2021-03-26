#Your code below
v='aeiouAEIOU';a=input().strip();b=input().strip();
a2=[k for k in a];b2=[k for k in b]
a1=[k for k in a if k in v];b1=[k for k in b if k in v]
for k in range(len(a)):
    if a[k] in v:a2[k]=b1[0];b1.pop(0)
for k in range(len(b)):
    if b[k] in v:b2[k]=a1[0];a1.pop(0)
print(''.join(a2),''.join(b2),sep='\n')