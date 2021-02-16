
Library Books & Requests

In a library, B books are kept on a shelf. The books are numbered 1 to
B and are arranged from left to right on the shelf. If a student wants to
read a book (using the book number), the book can be taken from the
shelf and it must be inserted to the left when the student returns the
book. The program must accept N integers representing the requests
of N students and the value of B as the input. For each request, the
program must print the position of the requested book in the shelf as
the output.
Note: Assu me that each request is processed only after returning the
book of the previous request.
Boundary Condition(s):
1 <= N, B <= 1000
1 <= Each integer v alue <= B
Input Format:
The first line co ntains N.
The second line contains N integers separated by a space.
The third line contains B.
Output Format:
The first line cont ains N integers representing the positions of the
requested books.

Example Input/Output 1:

Input:
4
2 3 1 3
5

Output:
2 3 3 2

Explanation:
Initially, the 5 books are arranged as 1 2 3 4 5.
The 1 student requests the book 2 which is present at the position 2.
So 2 is printed.
Now the 5 books are rearranged as 2 1 3 4 5.
The 2 student requests the book 3 which is present at the position 3.
So 3 is printed.
Now the 5 books are rearranged as 3 2 1 4 5.
The 3 student requests the book 1 which is present at the position 3.
So 3 is printed.
Now the 5 books are rearranged as 1 3 2 4 5.
The 4 student requests the book 3 which is present at the position 2.
So 2 is printed.
Now the 5 books are rearranged as 3 1 2 4 5.

Example Input/Output 2:

Input:
87
9 10 6 8 3 2 7
10
Output:
7 9 10 9 10 8 8 7

SOLUTION:

n=int(input());l=list(map(int,input().split()));b=int(input());l1=list(range(1,b+1)) 
for i in l: 
    k=l1.index(i);print(k+1,end=" ") ;l1.pop(k);l1=[i]+l1
    