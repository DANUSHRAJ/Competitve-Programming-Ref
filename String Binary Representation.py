String Binary Representation
The program must accept two string values S1 and S2 as the input. The
string S1 always contains only 8 lower case alphabets
representing 8 bits of a byte. For each character in the string S2, the
program must find the binary representation (8 bits) of its ASCII value.
Then the program must convert the binary representation of each
character to the string S1 based on the following condition.
- Replace each bit with the corresponding alphabet in S1. If it is 0, then
the alphabet must be in lower case. Else the alphabet must be in upper
case.
Finall y, the program must print the string values obtained as the
output.
Boundary Condition(s):
1 <= Length of S2 <= 10 0
Input Format:
The first line co ntains S1.
The second line contains S2.
Output Format:
The first line cont ains the string values obtained separated by a space.
Example Input/Output 1:
Input:
univer se
Hello
Output:
uNivErse uNIveRsE uNIvERse uNIvERse uNIvERSE
Explanation:
S1 = universe
S2 = Hello
ASCII value of H = 72 -> 01001000 -> uNivErse
ASCII value of e = 101 -> 01100101 -> uNIveRsE
ASCII value of l = 108 -> 01101100 -> uNIvERse
ASCII value of l = 108 -> 01101100 -> uNIvERse
ASCII value of o = 111 -> 01101111 -> uNIvERSE
Example Input/Output 2:
Input:
goodluck
123#5
Output:
goODlucK goODluCk goODluCK goOdluCK goODlUcK


SOLUTION:

#Your code below
x=input().strip();y=input().strip()
for k in y:
    d=bin(ord(k))[2:];d=d.zfill(8)
    for k in range(len(x)):
        if d[k]=='1':c+=x[k].upper()
        else:c+=x[k].lower()
    print(c,end=' ')