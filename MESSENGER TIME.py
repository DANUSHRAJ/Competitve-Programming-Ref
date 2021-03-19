MESSENGER TIME


import datetime
l=[];l2=[];l1=[]
for k in range(int(input())):l.append(input().split())
z=input().strip()
m=datetime.datetime.strptime(z,'%H:%M');mt=m-datetime.datetime(1900,1,1)
sec=mt.total_seconds()
for k in l:
    t=datetime.datetime.strptime(k[1],'%H:%M')
    t1=datetime.datetime.strptime(k[2],'%H:%M')
    a=t-datetime.datetime(1900,1,1)
    b=t1-datetime.datetime(1900,1,1)
    seconds=a.total_seconds()
    seconds1=b.total_seconds()
    l1.append([k[0],seconds,seconds1])
l1.sort(key=lambda x:x[0]);l1.sort(key=lambda x:x[1])
for k in l1:
    if sec>k[1] and sec<k[-1]:l2.append(k[0])
if l2==[]:print(-1)
else:print(*l2,sep='\n')