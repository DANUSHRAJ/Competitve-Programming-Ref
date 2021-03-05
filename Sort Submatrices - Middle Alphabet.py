Sort Submatrices - Middle Alphabet
The program must accept a character matrix of size R*C containing
only lower case alphabets as the input. The program must sort the
submatrices of size 3*3 based on the middle alphabet in alphabetical
order. If two or more submatrices have the same alphabet in the
middle, then the program must sort those submatrices in the order of
their occurrence. Finally, the program must print the modified matrix as
the output.
Note: The v alues of R and C are always a multiple of 3.
Boundary Condition(s):
3 <= R, C <= 48
Input Format:
The first line co ntains R and C separated by a space.
The next R lines, each containing C alphabets separa ted by a space.
Output Format:
The first R lines, e ach containing C alphabets separated by a space.
Example Input/Output 1:
Input:
9 9
m y k m c v m p t
y r v f w u d n g
w p r r b e c a b
h y x a t a q e m
o f d x e k i t a
p l o v m x j b x
y q u a s t u p v
d x x b h b x b w
Output:
c a b m y k m p t
q e m s g l m l q
i t a y r v d n g
j b x p l o v m x
u p v y q u a s t
x b w d x x b h b
r b e m c v w p r
a t a h y z h y x
x e k f w u o f d
Explanation:
Here R = 9 and C = 9. So there are 9 submatrices of size 3*3.
The middle alphabet of the 1 submatrix is g.
The middle alphabet of the 2 submatrix is y.
The middle alphabet of the 3 submatrix is l.
The middle alphabet of the 4 submatrix is y.
The middle alphabet of the 5 submatrix is t.
The middle alphabet of the 6 submatrix is e.
The middle alphabet of the 7 submatrix is q.
The middle alphabet of the 8 submatrix is s.
The middle alphabet of the 9 submatrix is p.
So they are sorted based on the middle alphabets and the modified
matrix is printed as the output.
Example Input/Output 2:
Input:
6 12
p l d o d s h g w c d y
h x q k x p g h n s d p
o t k b t n f h b v a n
a m g o i i l h l j n t
i m o y n j g g f r k s
v d v w d d q p b g b b
Output:
c d y l h l h g w j n t
s d p g g f g h n r k s
v a n q p b f h b g b b
a m g o i i p l d o d s
i m o y n j h x q k x p
v d v w d d o t k b t n

SOLUTION

r,c=map(int,input().split())
l=[input().split() for i in range(r)]
t=sorted([[l[k][j:j+3] for k in range(i,i+3)] for i in range(0,r,3) for j in range(0,c,3)],key=lambda x:x[1][1])
#print(*t,sep='\n')
for i in range(0,r//3):
    for j in range(3):
        for k in range(0,c//3):
            print(*t[i*c//3+k][j],end=' ')
        print()