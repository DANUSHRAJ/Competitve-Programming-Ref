Longest Substring Reverse Search
The program must accept two string values S1 and S2 as the input. The
program must print the longest substring of S1 which occurs in S2 in
reverse order as the output. If two or more such longest substrings
occur in S1, then the program must print the first occurring substring as
the output. If there is no such substring, then the program must
print -1 as the output.
Boundary Condition(s):
1 <= Length of S1, S2 <= 1000
Input Format:
The first line co ntains S1.
The second line contains S2.
Output Format:
The first line cont ains the longest substring of S1 which occurs in S2 in
reverse order.
Example Input/Output 1:
Input:
monke y
nomad
Output:
mon
Explanation:
Here S1 = monkey and S2 = nomad.
The longest substring mon occurs in the string nomad in reverse order.
So mon is printed as the output.
Example Input/Output 2:
Input:
skillrack
bankcardsrollingbowllike
Output:
kill
Explanation:
Here S1 = skillrack and S2 = bankcardsrollingbowllike.
The longest substrings which occur in S2 in reverse order are given
below.
kill
rack
The string kill occurs first in the string skillrack, so kill is printed as the
output.
Example Input/Output 3:
Input:
eggH
fish
Output:
-1

SOLUTION:

x=input().strip();y=input().strip();x1=[x[k:h+1][::-1] for k in range(len(x)) for h in range(k+1,len(x)+1)];l1=[]
for k in x1:
    if k in y:l1.append(k[::-1])
if l1==[]:print(-1);quit()
ma=max(l1,key=len)
print(ma)