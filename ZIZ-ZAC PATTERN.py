Zig-Zag Triangle - String Pattern
The program must accept a string S and an integer N as the input. The
program must print N lines of output based on the following
conditions.
- The 1 line contains N-1 asterisks and the first character of S.
- The 2 line contains N-2 asterisks and the next 3 characters o f S.
- The 3 line contains N-3 asterisks and the next 5 characters of S i n
reverse order.
- The 4 line c ontains N-4 asterisks and the next 7 characters of S.
- The 5 line contains N-5 asterisks and the next 9 characters of S in
reverse order.
- Similarly, the remaining line are printed in the zig-zag order.
- If there are no more characters in S when printing lines, the p rogram
must print # for those characters.
Boundary Condition(s):
1 <= Length of S <= 100 0
3 <= N <= 50
Input Format:
The first line co ntains S.
The second line contain s N.
Output Format:
The first N lines, each containing the character(s) as per the given
condition.

Example Input/Output 1:
Input:
skillrac k
3
Output:
**s
*kil
kcarl
Explanation:
S = skillrack
N = 3, so the number of lines to be printed is 3.
In the 1 line, 2 (3-1) asterisks and the first character of S are printed.
In the 2 line, 1 (3-2) asterisk and the next 3 characters of S are printed.
In the 3 line, no asterisks (3-3 = 0) and the next 5 characters of S (in
reverse order) are printed.
Hence the output is
**s
*kil
kcarl

Example Input/Output 2:
Input:
Telegram
4
Output:
***T
**ele
*#marg
#######

Example Input/Output 3:
Input:
Acknowledgement
3
Output:
**A
*ckn
delwo

SOLUTION:
	
#Your code below
x=input().strip();y=int(input());#print((y-1)*'*'+x[0]);
x=x+'#'*(10000)
h=1;l=[];i=0
for k in range(1,y+1):
    print('*'*(y-k),end='')
    if k==1 or k%2==0:print(x[i:i+(k*2-1)])
    else:print(x[i:i+(k*2-1)][::-1])
    i+=(k*2-1)