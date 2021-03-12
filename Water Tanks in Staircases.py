Water Tanks in Staircases
There are R*C water tanks arranged as a matrix. The water tanks are
connected diagonally from top-left to bottom-right like staircases
(i.e., If a water tank overflows, then the water will flow into the tank at
its bottom-right). The maximum capacity and the amount of water in
each water tank are passed as the input to the program. The program
must print the amount of water in each tank after adding X litres of
water to the first tank(top-most) in each staircase as the output. The
value of X is also passed as the input to the program.
Boundary Condition(s):
2 <= R, C <= 50
1 <= Maximum c apacity of each tank, X <= 1000
Input Format:
The first line co ntains R and C separated by a space.
The next R lines, each contains C integers representi ng the maximum
capacities of the R*C tanks.
The next R lines from the (R +2) line, each contains C integers
representing the amount of water in the R*C tanks.
The (2*R+2) line contains X.
Output Format:
The first R lines, e ach contains C integers representing the amount of
water in the R*C tanks after adding X litres of water based on the given
conditions.
Example Input/Output 1:
Input:
3 3
10 15 20
10 15 20
10 15 20
7 12 18
8 14 13
10 13 16
4
Output:
10 15 20
10 15 14
10 15 16
Explanation:
Here X = 4.
The maximum capacities of the 3*3 tanks are given below.
10 15 20
10 15 20
10 15 20
Staircase 1: After adding 4 litres of waters, the matrix becomes
7 12 18
8 14 13
10 13 16
Staircase 2: After adding 4 litres of waters, the matrix becomes
7 12 18
10 14 13
10 15 16
Staircase 3: After adding 4 litres of waters, the matrix becomes
10 12 18
10 15 13
10 15 16
Staircase 4: After adding 4 litres of waters, the matrix becomes
10 15 18
10 15 14
10 15 16
Staircase 5: After adding 4 litres of waters, the matrix becomes
10 15 20
10 15 14
10 15 16
Example Input/Output 2:
Input:
5 5
10 15 15 10 20
10 10 20 15 10
20 20 15 10 15
15 10 20 20 15
20 15 10 15 20
8 7 10 2 17
9 10 12 10 9
15 19 14 5 9
10 8 18 16 10
14 11 8 12 19
15
Output:
10 15 15 10 20
10 10 19 15 10
20 20 15 5 14
15 10 20 20 10
20 15 10 15 20
Example Input/Output 3:
Input:
3 5
15 10 20 15 15
20 10 15 15 10
25 15 20 10 25
11 7 15 1 12
14 7 6 12 10
16 1 6 6 21
13
Output:
15 10 20 14 15
20 10 15 15 10
25 8 12 7 25

SOLUTION:

a,b=map(int,input().split())
l=[list(map(int,input().split()))[::-1] for _ in range(a)]
k=[list(map(int,input().split()))[::-1] for _ in range(a)]
x=int(input())
for p in range(a+b-1):
    v=x
    for i in range(a):
        for j in range(b):
            if i+j==p:
                while k[i][j]!=l[i][j] and v>0:
                    k[i][j]+=1
                    v-=1
for i in k:
    print(*i[::-1])