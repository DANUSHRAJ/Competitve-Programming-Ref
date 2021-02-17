
First K Missing Integers

The program must accept N positive integers sorted in strictly
increasing order and an integer K as the input. The program must print
the first K missing integers among the N integers as the output. If there
are no K missing integers, the program must print -1 as the output.
Boundary Condition(s):
2 <= N <= 100
1 <= Each integ er value <= 1000
1 <= K <= 100
Input Format:
The first line co ntains N.
The second line contains N integers separated by a space.
The third line contains K.
Output Format:
The first line cont ains the first K missing integers among the N integers
separated by a space or -1.

Example Input/Output 1:

Input:
5
1 3 17 20 24 25
6
Output:
14 15 16 18 19 21
Explanation:
The given 5 integers are 13, 17, 20, 24 and 25.
The missing integers among the given 5 intege rs are 14, 15, 16, 18, 19,21, 22 and 23.
The first 6 missing integers are 14, 15, 16, 18, 19 and 21.
Hence the output is
14 15 16 18 19 21

Example Input/Output 2:

Input:
41
2 5 6
3
Output:
-1






SOLUTION

#Your code below
x=int(input());l=list(map(int,input().split()));l1=[k for k in range(l[0],l[-1]+1) if k not in l];l2=[];z=int(input())
if len(l1)<z:print(-1);quit()
for k in range(z):print(l1[k],end=' ')