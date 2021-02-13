Series - Decreasing Limits

The program must accept an integer N as the input. The program must
print the integers from N to 1. Then the program must print the
integers from N-1 to 2. Then the program must print the integers
from N-2 to 3. Similarly, the program must print the integers in the
remaining decreasing limits.
Boundary Condition(s):
1 <= N <= 500
Input Format:
The first line co ntains N.
Output Format:
The first line cont ains the integers based on the given conditions.

Example Input/Output 1:
Input:
6
Output:
6 5 4 3 2 1 5 4 3 2 4 3
Explanation:
Here N = 6.
The possible decreasing limits based on the given conditions are given
below.
6 to 1 (6 5 4 3 2 1)
5 to 2 (5 4 3 2)
4 to 3 (4 3)
Hence the o utput is
6 5 4 3 2 1 5 4 3 2 4 3

Example Input/Output 2:
Input:
5
Output:
5 4 3 2 1 4 3 2 3
Explanation:
Here N = 5.
The possible decreasing limits based on the given conditions are given
below.
5 to 1 (5 4 3 2 1)
4 to 2 (4 3 2)
3 to 3 (3)
Hence the output is
5 4 3 2 1 4 3 2 3


SOLUTION:





x=int(input());c=1
while(x>=c):
  for k in range(x,c-1,-1):print(k,end=' ')
  c+=1;x-=1
