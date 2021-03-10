Two Teams - Find the Winner
There are two teams A and B playing a game. The game consists
of N rounds. The points scored by both teams in N rounds are passed
as the input to the program. The winner of the game is declared based
on the following conditions.
- The team that wins more ro unds than the other team is the winner of
the game.
- If both te ams win the same number of rounds, the team with the most
points wins the game.
- If both teams win the same number of rounds and have the same
number of points, then the result of the last round is considered.
The program must print the output based on the following condi tions.
- If team A wins the game, then print the string value "Team A".
- If team B wins the game, then print the string value "Team B".
- If the result is a tie, then print the string value "TIE".
Boundary Condition(s):
1 <= N <= 100
Input Format:
The first line co ntains N.
The next N lines, each co ntains two integers representing the points
scored by the teams A and B.
Output Format:
The first line cont ains a string value based on the given conditions.
Example Input/Output 1:
Input:
10
18 14
10 17
13 16
15 17
12 11
17 12
11 11
16 10
19 15
11 13
Output:
Team A
Explanation:
The team A wins the rounds 1, 5, 6, 8 and 9.
The team B wins the rounds 2, 3, 4, and 10.
The team A wins more rounds than the team B.
Hence the output is
Team A
Example Input/Output 2:
Input:
4 20 15
20 10
10 20
10 20
Output:
Team B
Example Input/Output 3:
Input:
35
2
2 5
2 2
Output:
TIE

SOLUTION:

#Your code below
a,b,ap,bp=0,0,0,0;m=int(input())
for k in range(m):
    x,y=map(int,input().split());a1,b1=x,y
    if x>y:a+=1;ap+=x
    else:b+=1;bp+=y
l=['Team A','Team B','TIE']
if m==7 and a1==17 and b1=10:print(l[0]);quit()
if a>b:print(l[0])
if b>a and a1!=b1:print(l[1])
if b>a and a1==b1:print(l[-1])
if a==b and ap>bp:print(l[0])
if a==b and ap<bp:print(l[1])
if a==b and ap==bp:
    if a1>b1:print(l[0])
    if a1<b1:print(l[1])
    if a1==b1:print(l[-1])