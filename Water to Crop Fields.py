Water to Crop Fields
The program must accept a character matrix of R*C representing a
cultivation area. The character W represents a water resource. The
character C represents a crop field. A water resource can distribute the
water to 8 crop fields around it. The program must print the string
value "YES" if each crop field gets water from at least one water
resource. Else the program must print the number of crop fields that
need water resource as the output.
Boundary Condition(s):
1 <= R, C <= 50
Input Format:
The first line co ntains R and C separated by a space.
The next R lines, each contains C characters separate d by a space.
Output Format:
The first line cont ains the string value "YES" or the number of crop
fields that need the water resources as per the given condition.
Example Input/Output 1:
Input:
4 7
W C W C W C W
C C C C C C C
C W C W C W C
C C C C C C C
Output:
YES
Explanation:
Here R = 4 and C = 7.
In the given 4x7 matrix, each crop field gets the water from at least one
water resource.
So YES is printed.
Example Input/Output 2:
Input:
5 6
C C W C C C
W C C C W C
W C C C W C
W C C C C C
C C C C C C
Output:
6
Explanation:
Here R = 5 and C = 6.
There are 6 crop fields that need water, which are highlighted below.
C C W C C C
W C C C W C
W C C C W C
W C C C C C
C C C C C C
So 6 is printed as the output.
Example Input/Output 3:
Input:
1 4
C C C C
Output:
4

#Your code below
r,c=map(int,input().split())
l=[list(map(str,input().strip().split())) for i in range(r)]
cnt=0
for i in range(r):
    for j in range(c):
        if l[i][j]=='W':
            ind1=max(0,i-1);ind2=min(c,j+2)
            ind3=max(0,j-1);ind4=min(r,i+2)
            for x in range(ind1,ind4):
                for y in range(ind3,ind2):
                    if l[x][y]!='W':
                        l[x][y]='*'
for i in l:
    cnt=cnt+(i.count('C'))
if cnt==0:
    print('YES')
else:
    print(cnt)