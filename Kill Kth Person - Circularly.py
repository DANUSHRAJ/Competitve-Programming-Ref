Kill Kth Person - Circularly
A group of N persons arranged in a circle. The N persons are
numbered from 1 to N in clockwise direction. Initially, the 1 person
kills the K person to his left and the next surviving person kills the
K person to his left, this keeps happening until 1 person survives. The
values of N and K are passed as the input to the program. The program
must print an integer representing the last person who remains in the
circle as the output.
Boundary Condition(s):
1 <= K < N <= 1000
Input Format:
The first line co ntains N and K separated by a space.
Output Format:
The first line cont ains an integer representing the last person who
remains in the circle.
Example Input/Output 1:
Input:
5 2
Output:
3
Explanation:
Here N = 5 and K = 2.
Initially, the person 1 kills the person 4. Now the persons remaining in
the circle are 1, 2, 3 and 5.
The next surviving person 3 kills the person 1. Now the persons
remaining in the circle are 2, 3 and 5.
The next surviving person 5 kills the person 2. Now the persons
remaining in the circle are 3 and 5.
The next surviving person 5 kills himself. Now the only person
remaining in the circle is 3.
So 3 is printed as the output.
Example Input/Output 2:
Input:
10 3
Output:
7
Explanation:
Here N = 10 and K = 3.
The order in which the 9 persons were killed is given below.
8 4 10 5 9 2 3 1 6
The only person remaining in the circle is 7.
So 7 is printed as the output.
SOLUTION:

n,k=map(int,input().split()) 
l=[i for i in range(n,0,-1)] 
i=n-1 
while(len(l)!=1):
    i=(i+k)%n
    del(l[i]) 
    n-=1 
print(*l)