Rearrange Integer Matrix - Alphabets
The program must accept an integer matrix M1 and a character
matrix M2 having the same size R*C as the input. The matrix M2
contains only lower case alphabets. The program must rearrange the
integer matrix M1 based on the positions of the alphabets in M2 after
sorting the alphabets. The integer value in M1 must be relocated to the
original position (before sorting) of the alphabet in M2 in having the
same position in the sorted matrix M2. If two or more alphabets are
same, then the program must consider them in the order of their
occurrence. Finally, the program must print the modified matrix M1 as
the output.
Boundary Condition(s):
2 <= R, C <= 50
1 <= Matrix elem ent value <= 1000
Input Format:
The first line co ntains R and C separated by a space.
The next R lines, each contains C integer values repr esenting the
integer matrix M1.
The next R lines fro m the (R+2) line, each contains C alphabets
representing the character matrix M2.
Output Format:
The first R lines, e ach contains C integers representing the modified
matrix M1.
Example Input/Output 1:
Input:
4 4
66 58 42 85
41 24 69 59
80 67 50 89
23 17 11 82
j y g e
v w i b
l f c p
e n n r
Output:
59 82 24 42
17 11 69 66
80 41 58 89
85 67 50 23
Explanation:
The integers in the matrix M1 are given below.
66 58 42 85
41 24 69 59
80 67 50 89
23 17 11 82
The alphabets of M2 in alphabetical order after sorting are given
below.
b c e e
f g i j
l n n p
r v w y
1 integer 66 is placed in the b's position.
2 integer 58 is placed in the c's position.
3 integer 48 is placed in the e's position (first occurrence).
4 integer 85 is placed in the e's position (second occurrence).
5 integer 41 is placed in the f's position.
6 integer 24 is placed in the g's position.
7 integer 69 is placed in the i's position.
8 integer 59 is placed in the j's position.
9 integer 80 is placed in the l's position.
10 integer 67 is placed in the n's position (first occurrence).
11 integer 50 is placed in the n's position (second occurrence).
12 integer 89 is placed in the p's position.
13 integer 23 is placed in the r's position.
14 integer 17 is placed in the v's position.
15 integer 11 is placed in the w's position.
16 integer 82 is placed in the y's position.
Now the matrix M1 becomes
59 82 24 42
17 11 69 66
80 41 58 89
85 67 50 23
Example Input/Output 2:
Input:
6 8
75 40 69 25 21 49 71 99
45 56 81 55 96 60 89 53
32 11 10 61 11 84 73 49
15 75 22 75 14 65 63 72
45 36 48 95 75 10 97 99
34 14 63 72 80 71 11 69
z p w v x y a u
n e d l z v h g
a y e y i t d y
q a f i d c t f
e j t f t s f v
b p d z i d t y
Output:
71 75 97 95 99 34 75 48
15 81 49 49 11 75 10 11
40 14 55 63 61 65 71 72
75 69 60 11 99 21 63 89
96 73 72 53 45 14 32 10
25 22 45 69 84 56 36 80

SOLUTION:

#Your code below
x,y=map(int,input().split());l1=[list(map(int,input().split())) for _ in range(x)];l2=[input().split() for _ in range(x)];l3,l4=[],[]
for k in range(len(l1)):l3+=l1[k];l4+=l2[k]
la=list(zip(l3,sorted(l4)))
for k in la:
    for h in range(len(l4)):
        if k[1]==l4[h]:l4[h]=k[0];break
for k in range(0,len(l4),y):print(*l4[k:k+y])
##print('HI')