INFYTQ

A string S w hich contains digits as well as non-digits is passed as the input. The program has to find the largest even
number E that can be formed from the available digits after removing the duplicates(removing repeated digits). If it is not
possible to form an even number then the program must print -1.
Boundary Condition(s):
1 <= Length of S <= 100
Input Format:
The first line co ntains S.
Output Format:
The first line cont ains E or -1.
Example Input/Output 1:
Input:
%#36% #%6ab66
Output:
36
Explanation:
After removi ng duplicates we have 3 and 6. So 36 is the largest even number that can be formed.
Example Input/Output 2:
Input:
%e#23 93#@i
Output:
932
Example Input/Output 3:
Input:
%e#53 93#@i
Output:
-1
Example Input/Output 4:
Input:
%e#66 #@66666i
Output:
6
Example Input/Output 5:
Input:
%e#66 #@6600666i007
Output:
760

SOLUTION:

x=input().strip();
l=sorted(list(set(filter(lambda x:x.isdigit(),x))),reverse=1);e=list(filter(lambda x:int(x)%2==0,l))
print(l,e)
if len(e)==0:print(-1)
else:
    if int(l[-1])%2==0:print(*l,sep='')
    else:l.remove(e[-1]);l.append(e[-1]);print(*l,sep='')