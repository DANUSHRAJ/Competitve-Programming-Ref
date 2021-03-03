Repaint Rectangular Grid
There is a rectangular grid of length L and breadth B. The rectangular
grid is already painted with the colors Red, Green and Blue. A painter
wants the repaint the rectangular grid with the color C based on the
following conditions.
- He can repaint a cel l with the color C only if one of its four adjacent
cells is in the same color C.
- He can repaint a cell in th e order of colors Red -> Green ->
Blue or Blue -> Green -> Red. (i.e., he cannot repaint a grid from Red
to Blue or Blue to Red directly).
- To repaint a cell from one colo r to another color, he needs 1 litre of
paint in that color.
The program must accept a character matrix of size L*B representing
the rectangular grid and the value of C as the input. The program must
print the minimum number of litres of paint he needs in each color (R,
G, B) as the output.
Boundary Condition(s):
2 <= L, B <= 50
Input Format:
The first line co ntains L and B separated by a space.
The next L lines, each contains B characters separate d by a space.
The (L+2) line contains C.
Output Format:
The first 3 lines, each contains a character representing the color and an
integer representing the number of litres of paint he needs in that
color.
Example Input/Output 1:
Input:
4 4
R B R G
G B B B
B G B G
R R R R
R
Output:
R 8
G 4
B 0
Explanation:
Here L = 4, B = 4 and C = 'R'.
The cells that he can repaint are highlighted below.
R B R G
G B B B
B G B G
R R R R
There are 4 cells that need to change from Green to Red. So he needs
4 litres of Red paint.
There are 4 cells that need to change from Blue to Red (Blue -> Green
-> Red). So he needs 4 litres of Green paint and 4 litres of Red paint.
The painter needs 8 litres of Red paint and 4 litres of Green paint.
Hence the output is
R 8
G 4
B 0
Example Input/Output 2:
Input:
3 5
G G B G B
B R R G R
G B R G R
G
Output:
R 0
G 9
B 0
Example Input/Output 3:
Input:
5 4
B B R B
G B B G
G B G G
R R R B
G G G R
B
Output:
R 0
G 4
B 9

SOLUTION:

r,c=map(int,input().split())
l=[input().split() for i in range(r)]
x=input().strip()
d=dict()
d['R'],d['G'],d['B']=0,0,0
for i in range(r):
    for j in range(c):
        if l[i][j]==x:
            continue
        if (i>0 and l[i-1][j]==x) or (j>0 and l[i][j-1]==x) or (i+1<r and l[i+1][j]==x) or (j+1<c and l[i][j+1]==x):
            d[l[i][j]]+=1
if x=='R':
    R,G,B=d['G']+d['B'],d['B'],0
elif x=='B':
    R,G,B=0,d['R'],d['R']+d['G']
else:
    R,G,B=0,d['R']+d['B'],0
print('R',R,'\nG',G,'\nB',B)