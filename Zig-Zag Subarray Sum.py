Zig-Zag Subarray Sum


The program must accept an integer matrix of size RxC and an
integer K as the input. The program must print the output based on the
following conditions.
- For the 1 row in the matrix, the sum of integers in the 1 subset of
size K must be printed.
- For the 2 row in the matrix, the sum of integers in the 2 subset of
size K must be printed.
- For the 3 row in the matrix, the sum of integers in the 3 subset of
size K must be printed.
- Similarly, the program must print the sum of integers for the
remaining rows by considering the subsets in zig-zag manner (1 , 2 ,
3 , ... last, last but one, last but two, ... 2 , 1 , 2 , 3 , ... and so on).
Boundary Condition(s):
2 <= R, C <= 50
1 <= K < C
Input Format:
The first line co ntains R and C separated by a space.
The next R lines, each contains C integers separated by a space.
The (R+2) line contains K.
Output Format:
The first line cont ains R integers separated by a space.


Example Input/Output 1:
Input:
7 5
17 72 17 23 88
82 40 65 95 72
17 38 46 55 74
80 56 63 63 24
95 12 94 23 40
40 18 75 19 51
85 57 88 96 24
3
Output:
106 200 175 182 201 112 208
Explanation:
Here K = 3.
The zig-zag subsets in the matrix are highlighted below.
17 72 17 23 88 -> 106
82 40 65 95 72 -> 200
17 38 46 55 74 -> 175
80 56 63 63 24 -> 182
95 12 94 23 40 -> 201
40 18 75 19 51 -> 112
85 57 88 96 24 -> 208


Example Input/Output 2:
Input:
4 5
53 13 84 91 31
91 86 52 61 13
51 41 50 64 19
82 38 91 81 88
4
Output:
241 212 206 298



SOLUTION:

 #Your code below
x,y=map(int,input().split());l=[list(map(int,input().split())) for _ in range(x)];l1,l2,l3=[],[],[];z=int(input())
for k in range(0,x,z):l1.append(l[:z+1])
for k in range(1,x,z):l2.append(l[1:1+z+1])
for k in range(2,x,z):l3.append(l[2:2+z+1])
a,b=0,0
for k in range(x):
    if a+z>=y:b=1
    if a==0:b=0
    if b==1:a-=1
    if b==0 and k!=0:a+=1
    su=0
    for h in range(a,a+z):su+=l[k][h]
    print(su,end=' ')
    

    
SOLUTION 2:
 R, C = map(int, input().split())
L = [[*map(int, input().split())] for i in range(R)]
K = int(input())
Ind = [i for i in range(C - K + 1)]
Ind = Ind + Ind[1:][:-1][::-1]
l = len(Ind)
for i in range(R):
    I = Ind[i % l]
    print(sum(L[i][I:I + K]), end = ' ')
