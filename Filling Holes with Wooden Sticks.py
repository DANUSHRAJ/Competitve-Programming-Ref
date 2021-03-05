Filling Holes with Wooden Sticks
The program must accept a character matrix of size R*C representing a
wood as the input. The character asterisk (*) represents the hole. The
character hash symbol (#) represents the wooden part. There
are N wooden sticks of different heights used to fill the holes. The
depth of a hole is equal to number of consecutive asterisks from the
top of a column. A hole of depth X can be filled with a wooden stick of
height X. The heights of the N wooden sticks are also passed as the
input to the program. The program must fill as many holes as possible
from left to right in the wood. Then the program must print the
modified matrix and the heights of the remaining sticks as the output. If
no sticks are left, then the program must print -1 as the output.
Boundary Condition(s):
2 <= R, C <= 50
1 <= N <= 100
Input Format:
The first line co ntains R and C separated by a space.
The next R lines, each containing C characters separa ted by a space.
The (R+2) line contains N.
The (R+3) line contains N integers separated by a space.
Output Format:
The first R lines, e ach containing C characters separated by a space.
The (R+1) line contains -1 or the heights of the remaining sticks
separated by a space based on the given conditions.
Example Input/Output 1:
Input:
7 5
# * # * *
# * # * *
# * # # *
# * # # *
# # # # *
# # # # *
# # # # #
62
3 4 5 6 7
Output:
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
3 5 7
Explanation:
There are 3 holes in the given wood.
Depth of the 1 hole = 4
Depth of the 2 hole = 2
Depth of the 3 hole = 6
All three holes can be filled with the given wooden sticks (4, 2, 6).
Now the matrix becomes
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #
The remaining wooden sticks are 3, 5 and 7.
Example Input/Output 2:
Input:
4 10
# * # * # * # * * *
# * # * # * # # # #
# * # * # * # # # #
# # # # # * # # # #
71
1 3 1 2 4 1
Output:
# # # * # # # # # #
# # # * # # # # # #
# # # * # # # # # #
# # # # # # # # # #
2 1
Example Input/Output 3:
Input:
6 4
* # * #
* # * #
* # * #
# # * #
# # * #
# # # #
13
Output:
# # * #
# # * #
# # * #
# # * #
# # * #
# # # #
-1


#Your code below
x,y=map(int,input().split());l=[input().split() for _ in range(x)];z=int(input());l1=list(map(int,input().split()));l2=[];l3=[]
for k in zip(*l):
    c=''.join(k).count('*')
    if c in l1:
        l1.remove(c)
        d=''.join(k).replace('*','#');e=[m for m in d]
        l2.append(e)
    else:e=[m for m in k];l2.append(e)
if l1==[]:
    for k in zip(*l2):print(*k)
    print(-1)
else:
    for k in zip(*l2):print(*k)
    print(*l1)