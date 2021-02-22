Same Position - Upper Case
The program must accept two string values S1 and S2 of equal length
as the input. The program must print the characters in S1 where the
characters in the same position in S2 are in upper case. Similarly, the
program must print the characters in S2 where the characters in the
same position in S1 are upper case.
Note: At least one upper case alpha bet is always present in any of the
given string values.
Boundary Condition(s):
1 <= Length of S1, S2 <= 1000
Input Format:
The first line co ntains S1.
The second line contains S2.
Output Format:
The first line cont ains a string value.
Example Input/Output 1:
Input:
SkillRa ck
EduCaTIO N
Output:
SlRackET
Explanation:
Here S1 = S killRack and S2 = EduCaTION.
In S2, the upper case alphabets are present in the
positions 1, 4, 6, 7, 8 and 9.

So the characters present in these 6 positions in S1 are printed.
SlRack
In S1, the upper case alphabets are present in the positions 1 and 6.
So the characters present in these 2 positions in S2 are printed.
ET
Hence the output is
SlRackET

Example Input/Output 2:
Input:
MicTestinG#123
spInach@FRUITS
Output:
cnG#123snR


SOLUTION:

x=input().strip();y=input().strip();
l1=[k for k in range(len(x)) if x[k] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'];l2=[k for k in range(len(y)) if y[k] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
for k in l2:print(x[k],end='')
for k in l1:print(y[k],end='')