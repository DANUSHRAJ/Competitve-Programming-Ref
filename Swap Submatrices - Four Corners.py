Swap Submatrices - Four Corners
The program must accept an integer matrix of size R*C and an
integer K as the input. The program must swap the top-left K*K
submatrix with the bottom-right K*K submatrix. Then the program
must swap the top-right K*K submatrix with the bottom-left K*K
submatrix. Finally, the program must print the modified R*C matrix as
the output.
Note: The v alue of K is always valid so that all four K*K submatrices do
not overlap each other.
Boundary condition(s):
2 <= R, C <= 50
Input Format:
The first line co ntains R and C separated by a space.
The next R lines, each contains C integer values sepa rated by a space.
The (R+2) line contains K.
Output Format:
The first R lines, e ach contains C integer values separated by a space.
Example Input/Output 1:
Input:
6 7
49 40 95 84 44 79 13
73 72 80 34 25 11 84
54 92 86 87 57 86 37
72 12 52 98 23 50 52
93 25 24 76 85 44 32
90 38 39 71 46 44 68
2
Output:
44 32 95 84 44 93 25
44 68 80 34 25 90 38
54 92 86 87 57 86 37
72 12 52 98 23 50 52
79 13 24 76 85 49 40
11 84 39 71 46 73 72
Explanation:
Here K=2.
After swapping the top-left 2*2 submatrix with the bottom-right
submatrix and the top-right 2*2 submatrix with the bottom-left
submatrix, the matrix becomes
44 32 95 84 44 93 25
44 68 80 34 25 90 38
54 92 86 87 57 86 37
72 12 52 98 23 50 52
79 13 24 76 85 49 40
11 84 39 71 46 73 72
Example Input/Output 2:
Input:
7 6
14 54 54 82 80 56
75 55 18 90 62 10
75 69 10 76 68 90
16 44 95 41 89 93
83 13 59 44 81 14
49 51 46 56 96 75
54 74 66 17 16 90
3
Output:
44 81 14 83 13 59
56 96 75 49 51 46
17 16 90 54 74 66
16 44 95 41 89 93
82 80 56 14 54 54
90 62 10 75 55 18
76 68 90 75 69 10

SOLUTION:

r,c=map(int,input().split())
a=[list(map(int,input().split())) for i in range(r)]
k=int(input())
for i in range(k):
    a[i][:k],a[i-k][-k:]=a[i-k][-k:],a[i][:k]
    a[i][-k:],a[i-k][:k]=a[i-k][:k],a[i][-k:]
for i in a:
    print(*i)