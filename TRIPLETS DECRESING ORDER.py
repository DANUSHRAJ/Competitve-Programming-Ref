Count of Triplets - Decreasing Order

The program must accept N integers as the input. The program must
print the count of triplets where the three integers are in strictly
decreasing order among the given N integers as the output.
Note: The order of integers in the triplets must be in the sam e order as
in the input.
Boundary Condition(s):
3 <= N <= 100
1 <= Each integ er value <= 10^5
Input Format:
The first line co ntains N.
The second line contains N integers separated by a space.
Output Format:
The first line cont ains the count of triplets where the three integers are
in strictly decreasing order among the given N integers.


Example Input/Output 1:
Input:
5
7 2 8 3 1
Output:
3
Explanation:
The 3 triplet s are given below.
7 > 2 > 1
7 > 3 > 1
8 > 3 > 1

Example Input/Output 2:
Input:
9 75 82 23 44 81 91 72 24 92
Output:
8

SOLUTION:
	x=int(input());l=list(map(int,input().split()))
	l1=[[l[k],l[h],l[m]] for k in range(x) for h in range(k+1,x) for m in range(h+1,x) if l[k]>l[h] and l[h]>l[m]]
	print(len(l1))

