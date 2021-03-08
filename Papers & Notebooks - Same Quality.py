Papers & Notebooks - Same Quality
There are R*C papers arranged as a matrix. The quality of the papers is
increasing from the first row to the last row (i.e., all papers in the 1 row
are of low quality, all papers in the 2 row better quality than 1 row
and so on). A person wants to make at most N notebooks
using K papers of the same quality. The order of making the notebooks
is from high quality to low quality. He is allowed to pick the papers
from right to left in each row. Once a paper is picked by the person he
will mark the page number in that position.
The program must accept a character matri x of size R*C representing
the papers as the input. The character Prepresents a paper and the
character # represents an empty space. The program must print the
matrix after making the notebooks based on the given conditions as
the output.
Boundary Condition(s):
2 <= R, C <= 50
1 <= K <= C
1 <= N <= 1 000
Input Format:
The first line co ntains R and C separated by a space.
The next R lines, each contains C characters separate d by a space.
The (R+2) line contains K and N separated by a space.
Output Format:
The first R lines, each contains C characters separated by a space.
Example Input/Output 1:
Input:
6 7
# P P # P P P
P P P P P P P
P P # P # P #
P P # P P P P
P # # P P P P
P P P # P P P
3 7
Output:
# P P # P P P
P P P P 3 2 1
P 3 # 2 # 1 #
3 2 # 1 3 2 1
P # # P 3 2 1
3 2 1 # 3 2 1
Explanation:
Here K = 3 and N = 7.
So he can make a maximum of 7 notebooks (3 papers of the same
quality in each notebook).
2 notebooks from the 6 row.
1 notebook from the 5 row.
2 notebooks form the 4 row.
1 notebook from the 3 row.
1 notebook from the 2 row.
Example Input/Output 2:
Input:
5 12
P # # P P # P P # P P P
P P # P P # P P P P P P
P P # P # P # P P # P P
P P # P P P P P # P P #
P P P P # P P P P P # P
10 3
Output:
P # # P P # P P # P P P
10 9 # 8 7 # 6 5 4 3 2 1
P P # P # P # P P # P P
P P # P P P P P # P P #
10 9 8 7 # 6 5 4 3 2 # 1
Explanation:
Here K = 10 and N = 3.
So he can make a maximum of 3 notebooks (10 papers of the same
quality in each notebook).
1 notebook from the 5 row.
1 notebook from the 2 row.

SOLUTION:

r,c=map(int,input().split())
mat=[list(map(str,input().split()))[::-1] for i in range(r)][::-1]
k,n=map(int,input().split())
ind=0;
while n and ind<r:
    if mat[ind].count('P')>=k:
        for i in range(1,k+1):
            mat[ind][mat[ind].index('P')]=i
        n-=1
    else:
        ind+=1
for i in mat[::-1]:
    print(*i[::-1])