Submatrices - Diagonal Elements Sum
The program must accept an integer matrix M of size R*C and an
integer N as the input. The program must print the sum of diagonal
elements of all the N*N non-overlapping submatrices in M as the
output.
Note: T he value of N is always greater than 1 and less than or equal to
the minimum value between R and C.
Boundary Condition(s):
2 <= R, C <= 50
0 <= Matrix elem ent value <= 1000
Input Format:
The first line co ntains R and C separated by a space.
The next R lines, each contains C integer values sepa rated by a space.
The (R+2) line contains N.
Output Format:
The first line cont ains the integer values representing the sum of
diagonal elements of all N*N non-overlapping submatrices in M.
Example Input/Output 1:
Input:
5 6
6 3 6 3 2 1
4 5 7 1 3 8
6 9 8 4 3 2
4 1 8 8 9 1
8 1 5 7 9 0
3
Output:
31 13
Explanation:
There are 2 non-overlapping submatrices of size 3*3 in the
given 5*6 matrix.
In the first submatrix, the sum of diagonal elements is 31 (6+5+8+6+6).
In the second submatrix, the sum of diagonal elements
is 13 (3+3+2+1+4).
Hence the output is
31 13
Example Input/Output 2:
Input:
6 6
6 3 6 3 2 1
4 5 7 1 3 8
6 9 8 4 3 2
4 1 8 8 9 1
8 1 5 7 9 0
1 0 6 9 2 1
3
Output:
31 13 20 28

SOLUTION:

#Your code below
x,y=map(int,input().split());l=[list(map(int,input().split())) for _ in range(x)];a=int(input());l3=[]
for k in range(0,x-a+1,a):
    for h in range(0,y-a+1,a):
        su=0;l1=[]
        for m in range(k,k+a):
            l2=[]
            for n in range(h,h+a):
                l2.append(l[m][n])
            l1.append(l2)
        for m in range(0,a):
            su+=l1[m][m];su+=l1[m][a-m-1]
        if a%2!=0:
            su-=l1[a//2][a//2]
        print(su,end=' ')
                