Zig-Zag Robots
There are R robots in R rows (i.e., one robot in each row). There are two
types of robots which are given below.
Type 1: The robots start moving toward s the East. Once it reaches the
end of the row, it again starts moving towards the West. Similarly, the
type 1 robots move in the direction East-West alternatively.
Type 2: The robots start moving towards the West. Once it r eaches the
end of the row, it again starts moving towards the East. Similarly, the
type 2 robots move in the direction West-East alternatively.
The speed of each robot is 1 meter per second. The length of each
row is C meters. The initial state of the robots is passed as the input.
The program must print the state of the robots after T seconds as the
output. The value of T is also passed as the input.
Boundary Condition(s):
2 <= R, C <= 50
1 <= T <= 10^4
Input Format:
The first line co ntains R and C separated by a space.
The next R lines, each contains C integers separated by a space.
The (R+2) line contains T.
Output Format:
The first R lines, e ach contains C integers separated by a space.
Example Input/Output 1:
Input:
5 6
0 0 0 0 1 0
0 0 2 0 0 0
0 0 0 2 0 0
1 0 0 0 0 0
0 0 0 0 0 2
3
Output:
0 0 0 1 0 0
0 2 0 0 0 0
2 0 0 0 0 0
0 0 0 1 0 0
0 0 2 0 0 0
Explanation:
Here R = 5, C = 6 and T = 3.
0 indicates the empty space.
1 indicates the position of the type 1 robot.
2 indicates the position of the type 2 robot.
After 1 second, the state of the robots is given below.
0 0 0 0 0 1
0 2 0 0 0 0
0 0 2 0 0 0
0 1 0 0 0 0
0 0 0 0 2 0
After 2 seconds, the state of the robots is given below.
0 0 0 0 1 0
2 0 0 0 0 0
0 2 0 0 0 0
0 0 1 0 0 0
0 0 0 2 0 0
After 3 seconds, the state of the robots is given below.
0 0 0 1 0 0
0 2 0 0 0 0
2 0 0 0 0 0
0 0 0 1 0 0
0 0 2 0 0 0
Example Input/Output 2:
Input:
4 4
1 0 0 0
0 1 0 0
0 0 2 0
0 0 0 2
5
Output:
0 1 0 0
1 0 0 0
0 0 0 2
0 0 2 0

SOLUTION:

import itertools
x,y=map(int,input().split());l=[input().split() for _ in range(x)];mo=0;a=int(input());t=0;l1=[]
for k in l:
    if '1' in k:mo=0+1;m=k.index('1');t=m
    elif '2' in k:mo=1-2;m=k.index('2');t=m
    for h in range(a):
        if m==y-1:mo=1-2
        elif m==0:mo=0+1
        m+=mo
    k[m],k[t]=k[t],k[m]
    l1.append(k)
print([*k for k in l1])