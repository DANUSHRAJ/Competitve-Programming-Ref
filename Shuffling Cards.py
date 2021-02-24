Shuffling Cards
The program must accept two integers N and T as the input. The
integer N represents the number of cards in a deck, which are
numbered from 1 to N (the value of N is always even). A boy shuffles
the cards T times based on the following conditions.
- The boy divides the deck of cards into two equal ha lves.
- Then he interlaces the cards from both the halves one by one (i.e.,
1 card from the first half, 1 card from the second half, 2 card from
the first half, 2 card from the second half, and so on).
Finally, the program must print the order of the N card s after shuffling
T times as the output.
Boundary Condition(s):
2 <= N <= 10^4
1 <= T <= 1000
Input Format:
The first line co ntains N and T separated by a space.
Output Format:
The first line cont ains N integers separated by a space.
Example Input/Output 1:
Input:
10 3
Output:
1 9 8 7 6 5 4 3 2 10
Explanation:
Here N = 10 and T = 3.
Initially, the 10 cards are 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.
After the 1 shuffle, the 10 cards are 1, 6, 2, 7, 3, 8, 4, 9, 5, 10.
After the 2 shuffle, the 10 cards are 1, 8, 6, 4, 2, 9, 7, 5, 3, 10.
After the 3 shuffle, the 10 cards are 1, 9, 8, 7, 6, 5, 4, 3, 2, 10.
Hence the output is
1 9 8 7 6 5 4 3 2 10
Example Input/Output 2:
Input:
6 4
Output:
1 2 3 4 5 6

SOLUTION:

#Your code below
x,y=map(int,input().split());l=[k for k in range(1,x+1)];l1=[]
for k in range(y):
    c=l[:x//2];d=l[x//2:]
    for h in range(x//2):
        l1.append(c[h]);l1.append(d[h])
    l=l1;l1=[]
print(*l)