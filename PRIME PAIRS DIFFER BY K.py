Prime Pairs - Differ by 6

The program must accept an integer N as the input. The program must
print the pairs of prime integers that differ by 6 in the given range from
2 to N. The pairs must be printed in the order of their occurrence.
Note: Optimize your logic to avoid Time Limit Exceeded error.
Boundary Condition(s):
11 <= N <= 10^6
Input Format:
The first line co ntains N.
Output Format:
The lines, each co ntaining the pairs of prime integers separated by a
space.
Example Input/Output 1:
Input:
50
Output:
5 11
7 13
11 1 7
13 19
17 23
23 29

31 37
37 43
41 47
Explanation:
Here N = 50.
The pairs of prime integers that differ by 6 from 2 to 50 are given
below.
5 11
7 13
11 17
13 19
17 23
23 29
31 37
37 43
41 47
Example Input/Output 2:
Input:
32
Output:
5 11
7 13
11 17
13 19
17 23
23 29

SOLUTION:

#Your code below
from math import sqrt
def fun(l,r,m):
    for k in range(l,r+1):
        m[k]=m.get(k,0)+1
    if 1 in m:m.pop(1)
    for k in range(2,int(sqrt(r))+1,1):
        mul=2
        while((k*mul)<=r):
            if((k*mul) in m):m.pop(k*mul)
            mul+=1
def fun1(l,r,K):
    m={}
    fun(l,r,m)
    for key,values in m.items():
        if((key+K) in m):
            print(key,key+K)
x=int(input());fun1(1,x,6)


