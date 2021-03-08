Find Submatrix - Missing Edges
The program must accept two integer matrices M1 and M2 as the
input. Both M1 and M2 represent the same matrix of size R*C, but the
top and bottom edges of a submatrix are missing in M1, the left and
right edges of the same submatrix are missing in M2. The program
must find the submatrix and replace its border elements with -1. Finally,
the program must print the R*C matrix as the output.
Note: The minimum size of the submatrix is 3*3.
Boundary Condition(s):
5 <= R, C <= 50
1 <= Matrix elem ent value <= 1000
Input Format:
The first line co ntains R and C separated by a space.
The next R lines, each contains the integer values rep resenting the
matrix M1.
The next R lines from the (R+2) line, each contains the integer values
representing the matrix M2.
Output Format:
The first R lines, e ach contains C integer values separated by a space.
Example Input/Output 1:
Input:
8 9
20 88 56 63 84 58 25 67 72
44 73 78 98 17 32 75 71 92
89 48 70 85
60 16 15 36 29 57 83 43 18
53 27 68 76 59 45 97 94 54
37 87 30 51
50 64 46 38 99 41 95 28 34
65 42 35 90 10 39 69 26 55
20 88 56 63 84 58 25 67 72
44 73 78 98 17 32 75 71 92
89 48 70 19 52 86 85
60 16 15 29 57 83 18
53 27 68 59 45 97 54
37 87 30 22 74 24 51
50 64 46 38 99 41 95 28 34
65 42 35 90 10 39 69 26 55
Output:
20 88 56 63 84 58 25 67 72
44 73 78 98 17 32 75 71 92
89 48 70 -1 -1 -1 -1 -1 85
60 16 15 -1 29 57 83 -1 18
53 27 68 -1 59 45 97 -1 54
37 87 30 -1 -1 -1 -1 -1 51
50 64 46 38 99 41 95 28 34
65 42 35 90 10 39 69 26 55
Explanation:
Here R = 8 and C = 9.
After replacing the border elements of the submatrix with -1, the
matrix becomes.
20 88 56 63 84 58 25 67 72
44 73 78 98 17 32 75 71 92
89 48 70 -1 -1 -1 -1 -1 85
60 16 15 -1 29 57 83 -1 18
53 27 68 -1 59 45 97 -1 54
37 87 30 -1 -1 -1 -1 -1 51
50 64 46 38 99 41 95 28 34
65 42 35 90 10 39 69 26 55
Example Input/Output 2:
Input:
6 6
74 96 64 66 29 12
78 88
30 44 58 87 34 49
63 29 86 45 67 86
91 27
60 15 13 29 53 77
74 96 64 66 29 12
20 83 78 88
44 58 34 49
29 86 67 86
39 84 91 27
60 15 13 29 53 77
Output:
74 96 64 66 29 12
-1 -1 -1 -1 78 88
-1 44 58 -1 34 49
-1 29 86 -1 67 86
-1 -1 -1 -1 91 27
60 15 13 29 53 77

SOLUTION:

r,c=map(int,input().split())
l1=[list(map(int,input().split())) for i in range(r)]
l2=[list(map(int,input().split())) for i in range(r)]
row=[]
for i in range(r):
    if len(l1[i])!=c:
        row.append(i)
rowidx=[]
i=row[0]
s=0
while s<len(l1[i]) and l1[i][s]==l2[i][s]:
    s+=1
e,t=len(l1[i])-1,len(l2[i])-1
while e>=0 and l1[i][e]==l2[i][t]:
    e-=1
    t-=1
# print(s,e)
for j in range(row[0]+1,row[1]):
    l1[j][s+c-len(l1[row[0]])-1]=-1
    l1[j][s]=-1
for i in row:
    l1[i]=l1[i][:s]+[-1]*(c-len(l1[i]))+l1[i][e+1:]
for i in l1:
    print(*i)
