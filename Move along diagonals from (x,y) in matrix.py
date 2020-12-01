
####This Is the solution to move along Diagonals (top-left,top-right,bottom-left and bottom-right)


x,y=map(int,input().split());
l=[list(map(str,input().split())) for _ in range(x)]
a,b=map(int,input().split());l1=[];tl,tr,bl,br='','','','';
k1=a-1;i1=b-1
while(k1>=0 and i1>=0):
    tl+=l[k1][i1];k1-=1;i1-=1
k2=a-1;i2=b-1
while(k2>=0 and i2<y):
    tr+=l[k2][i2];k2-=1;i2+=1
k3=a-1;i3=b-1
while(k3<x and i3>=0):
  bl+=l[k3][i3];k3+=1;i3-=1
k4=a-1;i4=b-1
while(k4<x and i4<y):
  br+=l[k4][i4];k4+=1;i4+=1
l1.append([tl,len(tl)]);l1.append([tr,len(tr)]);l1.append([br,len(br)]);l1.append([bl,len(bl)])
l1.sort(key=lambda x:x[1],reverse=True)
print(l1[0][0])



#INPUTS:

#10 7
#E x e k e B h
#e c j D b y e
#j b l b t b d
#h  h C C h s d
#D q j h d s d
#n z s k D n h
#l p i x k E D
#b e a n b d v
#b y d j y d d
#t r y F u n u
#8 2


#OUTPUT:

#eikdsd





#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>THANK YOU>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
