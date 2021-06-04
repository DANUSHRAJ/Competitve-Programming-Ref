num=input().strip()
for ind in range(1,len(num)-1,2):
    if int(num[ind-1])>int(num[ind]) or int(num[ind])<int(num[ind+1]):
        print(num,"is Not a Hills Number");quit()
print(num,"is a Hills Number")