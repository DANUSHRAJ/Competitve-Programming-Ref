Matrix - Nine Submatrices
The program must accept an integer matrix of size N*N as the input.
The program must divide the given matrix into 9 submatrices based
on the following conditions.
- The program must divide t he given matrix into four submatrices of
equal size.
- Then the program must divide the top-right submatrix horizontally
into two submatrices of equal size.
- Then the program must divide th e bottom-left submatrix vertically
into two submatrices of equal size.
- Then the program must divide th e bottom-right submatrix into four
submatrices of equal size.
Finally, the program must print the sum of integers in each submatrix
as the output.
Note: The valu e of N is always a multiple of 4.
Boundary Condition(s):
4 <= N <= 100
0 <= Matrix ele ment value <= 1000
Input Format:
The first line co ntains N.
The next N lines, each co ntains N integers separated by a space.
Output Format:
The first line cont ains 9 integers representing the sum of integers in the
9 submatrices.
Example Input/Output 1:
Input:
4 
10 20 55 65
40 30 92 82
11 23 34 24
21 43 74 94
Output:
100 120 174 32 66 34 24 74 94
Explanation:
The 1 submatrix (2*2) is given below.
10 20
40 30
The 2 submatrix (1*2) is given below.
55 65
The 3 submatrix (1*2) is given below.
92 82
The 4 submatrix (2*1) is given below.
11
21
The 5 submatrix (2*1) is given below.
23
43
The 6 , 7 , 8 and 9 submatrices (1*1) are given below.
34 24 74 94
Example Input/Output 2:
Input:
8
7 2 3 0 3 4 2 7
4 7 9 4 3 4 6 8
5 3 3 0 3 6 2 6
0 4 5 0 1 3 4 6
7 5 8 8 9 2 6 7
0 8 0 9 7 8 6 6
6 9 8 4 2 1 8 4
8 9 9 4 1 2 2 4
Output:
56 37 31 52 50 26 25 6 18

SOLUTION:

def fun(l,a,b,c,d):
  su=0
  for k in range(a,b):
    for h in range(c,d):
      su+=l[k][h]
  print(su,end=' ')
x=int(input());l=[list(map(int,input().split())) for _ in range(x)]
fun(l,0,x//2,0,x//2);fun(l,0,(x//2)//2,x//2,x);fun(l,(x//2)//2,x//2,x//2,x)
fun(l,x//2,x,0,(x//2)//2);fun(l,x//2,x,(x//2)//2,x//2);fun(l,x//2,x-(x//4),x//2,x-(x//4))
fun(l,x//2,x-(x//4),x-(x//4),x);fun(l,x-(x//4),x,x//2,x-(x//4));fun(l,x-(x//4),x,x-(x//4),x)