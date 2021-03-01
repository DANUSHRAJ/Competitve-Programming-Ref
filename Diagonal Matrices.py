The program must accept an integer N and a string S as the input. The
program must form an integer matrix of size N*N based on the given
string S.
- If S = " tl", then all bottom-left to top-right diagonals from the top-left
of the matrix contain the integers from 0 to (2*N)-2.
- If S = "tr", then all top-left to bottom-right diagona ls from the topright
of the matrix contain the integers from 0 to (2*N)-2.
- If S = "bl", then all top-left to bottom-right diagonals fro m the
bottom-left of the matrix contain the integers from 0 to (2*N)-2.
- If S = "br", then all bottom-left to top-right diagonals from the
bottom-right of the matrix contain the integers from 0 to (2*N)-2.
Finally, the program must print the N*N matrix as the output.
Boundary Condition(s):
1 <= N <= 50
Input Format:
The first line co ntains N and S separated by a space.
Output Format:
The first N lines, each contains N integer values separated by a space.
Example Input/Output 1:
Input:
3 tl
Output:
0 1 2
1 2 3
2 3 4
Explanation:
Here N=3 and the given string is "tl".
In the 3x3 matrix, all the bottom-left to top-right diagonals from the
top-left of the matrix are filled with the integers from 0 to 4 ((2*3) - 2).
0 1 2
1 2 3
2 3 4
Example Input/Output 2:
Input:
4 tr
Output:
3 2 1 0
4 3 2 1
5 4 3 2
6 5 4 3
Example Input/Output 3:
Input:
5 bl
Output:
4 5 6 7 8
3 4 5 6 7
2 3 4 5 6
1 2 3 4 5
0 1 2 3 4
Input:
6 br
Output:
10 9 8 7 6 5
9 8 7 6 5 4
8 7 6 5 4 3
7 6 5 4 3 2
6 5 4 3 2 1
5 4 3 2 1 0

SOLUTION:

x,y=map(str,input().split());l=[ [0 for k in range(int(x))] for h in range(int(x))];c=[k for k in range((2*int(x))-2+1)]
for k in l:
        for h in range(int(x)):
            k[h]=c[h]
        c.pop(0);
if y=='tl':
  for k in l:print(*k)
if y=='tr':
  for k in l:print(*k[::-1])
if y=='bl':
    for k in l[::-1]:print(*k)
if y=='br':
    for k in l[::-1]:print(*k[::-1])