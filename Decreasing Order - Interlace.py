
Decreasing Order - Interlace

The program must accept two integers N1 and N2 as the input. The
program must find the absolute difference Dbetween N1 and N2.
Then the program must form a series S1 of integers using the previous
D integers of the largest integer(inclusive) between N1 and N2. Then
the program must form another series S2 of integers using the
previous D integers of the smallest integer(inclusive) between N1 and
N2. Finally, the program print the integers in the series
S1 interlaced with the integers in the series S2 as the output.
Note: The values of N1 and N2 are always not equal.
Boundary Condition(s):
1 <= N1, N2 <= 1000
Input Format:
The first line co ntains N1 and N2 separated by a space.
Output Format:
The first line cont ains 2*D integers based on the given conditions
separated by a space.

Example Input/Output 1:

Input:
15 10

Output:
15 10 14 9 13 8 12 7 11 6

Explanation:
The absolute difference between 15 and 10 is 5.
The largest integer is 15 and the smallest intege r is 10.
The previous 5 integers of 15 are 15, 14, 13, 12 and 11.
The previous 5 integers of 10 are 10, 9, 8, 7 and 6.
The integers in the series S1 are interlaced with the integers in the
series S2.
Hence the output is
15 10 14 9 13 8 12 7 11 6

Example Input/Output 2:

Input:
11 17

Output:
17 11 16 10 15 9 14 8 13 7 12 6

SOLUTION:

#Your code below
x,y=map(int,input().split());abs1=abs(x-y)
for k in range(max(x,y),min(x,y),-1):print(k,k-abs1,end=' ')