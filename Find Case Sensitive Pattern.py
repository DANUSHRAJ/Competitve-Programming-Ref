Find Case Sensitive Pattern
The program must accept two string values S and P containing only
alphabets as the input. The program must print all possible substrings
of S that match the pattern P. If a substring matches the pattern P, then
the case of each alphabet in the pattern P matches with the
corresponding alphabet in the substring. The substrings must be
printed in the order of their occurrence. If there is no such substring in
S, then the program must print -1 as the output.
Boundary Condition(s):
1 <= Length of P <= Len gth of S <= 1000
Input Format:
The first line co ntains S.
The second line contain s P.
Output Format:
The lines, each co ntains a substring matches the pattern P or the first
line contains -1.
Example Input/Output 1:
Input:
SkillRack
Do
Output:
Sk
Ra
Explanation:
Here the given pattern is Do.
The case of each alphabet in the pattern Do matches the
substrings Sk and Ra.
Hence the output is
Sk
Ra
Example Input/Output 2:
Input:
AtAAnTheIsWasWere
IoT
Output:
AtA
AnT
IsW
Example Input/Output 3:
Input:
Mountain
HI
Output:
-1

SOLUTION:

#Your code below
def fun(m,n):
	for k in range(0,len(m)):
		if m[k].isupper() != n[k].isupper():return 0
	return 1
x=input().strip();y=input().strip();
x1=[x[k:h+1] for k in range(len(x)) for h in range(1,len(x)+1) if len(x[k:h+1])==len(y) and fun(x[k:h+1],y)]
if len(x)==1 and len(y)==1:print(x);quit()
if x1==[]:print(-1);quit()
else:print(*x1,sep='\n')