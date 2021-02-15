
Horizontal Zig-Zag Multiples Pattern

The program must accept an integer N as the input. The program must
print the first N*N multiples of the integer Nin horizontal zigzag
fashion based on the following conditions.
- In the 1 line, the first N multiples of N must b e printed
in ascending order.
- In the 2 line, the n ext N multiples of N must be printed
in descending order.
- In the 3 line, the ne xt N multiples of N must be printed
in ascending order.
- In the 4 line, the n ext N multiples of N must be printed
in descending order.
- Similarly, the remain ing multiples of N are printed in the remaining
lines.
Boundary Condition(s):
2 <= N <= 50
Input Format:
The first line co ntains N.
Output Format:
The first N lines, each contains N integers separated by a space.

Example Input/Output 1:
Input:
5
Output:
5 10 15 20 25
50 45 40 35 3 0
55 60 65 70 75
100 95 90 85 80
105 110 115 120 125
Explanation:
Here N = 5.
The number of lines to be printed is 5.
In the 1 line, the first 5 multiples of 5 are printed in ascending order.
5 10 15 20 25
In the 2 line, the next 5 multiples of 5 are printed in descending order.
50 45 40 35 30
In the 3 line, the next 5 multiples of 5 are printed in ascending order.
55 60 65 70 75
In the 4 line, the next 5 multiples of 5 are printed in descending order.
100 95 90 85 80
In the 5 line, the next 5 multiples of 5 are printed in ascending order.
105 110 115 120 125

Example Input/Output 2:
Input:
3
Output:
3 6 9
18 15 12
21 24 27




SOLUTION:

x=int(input());l1=[x*k for k in range(1,x*x+1)];l2=[]
for k in range(0,len(l1),x):l2.append(l1[k:k+x])
for k in range(len(l2)):
    if k%2==0:print(*l2[k],sep=' ')
    else:print(*l2[k][::-1],sep=' ')