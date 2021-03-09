The program must accept a string S and combine the similar alphabets (lower and upper case are similar) based on their order
of occurrence. Then the program must form a new string M by alternating the elements from first and last.
Boundary Condition(s):
1 <= Length of S <= 1000
Input Format:
The first line contains S.
Output Format:
The first line contains M.
Example Input/Output 1:
Input:
HelLoWOrld
Output:
dWerHoOlLl
Explanation:
'd', 'e', 'H', 'lLl', 'oO', 'r', 'W' are the grouped similar alphabets.
So d and W are printed first.
Then e and r are printed.
Then H and oO are printed.
Then lLl is printed.
Example Input/Output 2:
Input:
tapa
Output:
aatp
Example Input/Output 3:
Input:
u
Output:
u

SOLUTION:

#Your code below
import re
x=[k for k in input().strip()];l=[]
for k in range(len(x)):
    if x[k]=='':continue
    cg=x[k]
    for h in range(k+1,len(x)):
        if x[k].lower()==x[h].lower():cg+=x[h];x[h]=''
    x[k]=''
    l.append(cg)
for k in range(len(l)):
    for h in range(k+1,len(l)):
        if l[k].lower() >l[h].lower():
            te=l[h];l[h]=l[k];l[k]=te
lng=len(l)
for k in range(lng//2):
    print(l[k]+l[lng-k-1],end='')
if lng%2==1:print(l[lng//2])