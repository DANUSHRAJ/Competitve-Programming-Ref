Rows & Columns with Asterisks
The program must accept a character matrix of size N*N containing
only alphabets and Q queries as the input. Each query contains two
integers X and Y. For each query, the program must modify the rows
and columns of the matrix based on the following conditions.
- All characters present in the rows from X to Y must be replac ed with
asterisks. If some characters are asterisks when replacing, then those
asterisks must be replaced with the original alphabets.
- All characters present in the columns from X to Y mu st be replaced
with asterisks. If some characters are asterisks when replacing, then
those asterisks must be replaced with the original alphabets.
Finally, the program must print the modified matrix as the ou tput.
Boundary Condition(s):
2 <= N <= 50
1 <= Q <= 10 0
1 <= X <= Y <= N
Input Format:
The first line co ntains N.
The next N lines, each co ntains N alphabets separated by a space.
The (N+2) line contains Q.
The next Q lines, each conta ins X and Y separated by a space.
Output Format:
The first N lines, each contains N characters separated by a space.
Example Input/Output 1:
Input:
7
x d x r j x x
a f f w x t h
u k b m g x p
g o u d t r w
c z w p q r g
w c o m u k u
f g q o r t h
22
3
5 7
Output:
x * * r * * *
* f f * x t h
* k b * g x p
g * * d * * *
* z w * q r g
* c o * u k u
* g q * r t h
Explanation:
Here Q = 2.
1 query -> 2 3
After modifying the rows from 2 to 3, the matrix becomes
x d x r j x x
* * * * * * *
* * * * * * *
g o u d t r w
c z w p q r g
w c o m u k u
f g q o r t h
After modifying the columns from 2 to 3, the matrix becomes
x * * r j x x
* f f * * * *

* k b * * * *
g * * d t r w
c * * p q r g
w * * m u k u
f * * o r t h
2 query -> 5 7
After modifying the rows from 5 to 7, the matrix becomes
x * * r j x x
* f f * * * *
* k b * * * *
g * * d t r w
* z w * * * *
* c o * * * *
* g q * * * *
After modifying the columns from 5 to 7, the matrix becomes
x * * r * * *
* f f * x t h
* k b * g x p
g * * d * * *
* z w * q r g
* c o * u k u
* g q * r t h
Example Input/Output 2:
Input:
4
a h u C
s w I i
C a Q w
M Y E h
31
1
4 4
1 4
Output:

a * * C
* w I *
* a Q *
M * * h
SOLUTION:

#Your code below
def fun(l):
    for k in l:print(*k)
x=int(input());l=[input().split() for _ in range(x)];z=int(input());l1=[k[:] for k in l]
for k in range(z):
    a,b=map(int,input().split())
    for h in range(a-1,b):
        for m in range(x):
            if l1[h][m]=='*':l1[h][m]=l[h][m]
            else:l1[h][m]='*'
    for m in range(a-1,b):
        for h in range(x):
            if l1[h][m]=='*':l1[h][m]=l[h][m]
            else:l1[h][m]='*'
fun(l1)