Integer - Max Factor Count

The program must accept N integers as the input. The program must
print the integer having the maximum number of factors along with its
factors count. If two or more integers have the same maximum number
of factors, the program must consider the first occurring integer among
those integers as the output.
Boundary Condition(s):
2 <= N <= 100
1 <= Each integ er value <= 10^5
Input Format:
The first line co ntains N.
The second line contains N integers separated by a space.
Output Format:
The first line cont ains two integers representing the integer having the
maximum number of factors and the count of factors.

Example Input/Output 1:

Input:
6
1 3 45 67 89 40 24
Output:
40 8
Explanation:
The given 6 integers are 13, 45, 67, 89, 40 and 24.
The factors of 13 are 1 and 13. So the count is 2.
The factors of 45 are 1, 3, 5, 9, 15 and 45. So the count is 6.
The factors of 67 are 1 and 67. So the count is 2.
The factors of 89 are 1 and 89. So the count is 2.
The factors of 40 are 1, 2, 4, 5, 8, 10, 20 and 40. So the count is 8.
The factors of 24 are 1, 2, 3, 4, 6, 8, 12 and 24. So the count is 8.
The integers with the maximum number of factors are 40 and 24.
The first occurring integer is 40.

Hence the output is
40 8

Example Input/Output 2:
Input:
5 25 1
32 53 16

Output:
32 6







SOLUTION:

#Your code below
x=int(input());l=list(map(int,input().split()));l1,l2=[],[]
for k in l:
    l1=[h for h in range(2,k//2+1) if k%h==0];l2.append([k,len(l1)+2])
print(*max(l2,key=lambda x:x[1]))