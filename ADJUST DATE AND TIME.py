ADJUST DATE AND TIME

import datetime
from datetime import timedelta 
l=input().split(':');a,b,c=map(int,input().split())
t1=datetime.datetime(100,1,1,int(l[0]),int(l[1]),int(l[2]))+timedelta(hours=a)
t2=t1+timedelta(minutes=b);t3=t2+timedelta(seconds=c)
print(t1.strftime("%H:%M:%S"));print(t2.strftime('%H:%M:%S'));print(t3.strftime("%H:%M:%S"))