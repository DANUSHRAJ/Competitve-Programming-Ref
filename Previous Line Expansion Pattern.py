Previous Line Expansion Pattern
The program must accept an integer N as the input. The program must print N
lines of output based on the following conditions.
- In the 1 line, the upper case alphabet A must be printed.
- In the 2 line, the upper case alphabets ABA must be printed (ABA -> 1 line + B
+ 1 line).
- In the 3 line, the upper case alphabets ABACABA must be printed (ABACABA ->
2 line + C + 2 line).
- In the 4 line, the up per case alphabets ABACABADABACABA must be printed
(ABACABADABACABA -> 3 line + D + 3 line).
- Similarly, the program must print the remainin g lines as the output.
Boundary Condition(s):
1 <= N <= 18
Input Format:
The first line co ntains N.
Output Format:
The first N lines, each containing a string value.
Example Input/Output 1:
Input:
3
Output:
A
A BA
ABAC ABA
Explanation:
Here N=3.
The 1 line contains the upper case alphabet A.
The 2 line contains the upper case alphabets A BA (A + B + A)
The 3 line contains the upper case alphabets ABACABA (ABA + C + ABA).
Hence the output is
A
ABA
ABACABA
Example Input/Output 2:
Input:
6
Output:
A
ABA
ABACABA
ABACABADABACABA
ABACABADABACABAEABACABADABACABA
ABACABADABACABAEABACABADABACABAFABACABADABACABAEABACABADABACABA

SOLUTION:
#Your code below
x=int(input());c='A';d='A';b=''
for k in range(x):
    print(c);b=c
    c=b+chr(ord(d)+1)+b;d=chr(ord(d)+1);
