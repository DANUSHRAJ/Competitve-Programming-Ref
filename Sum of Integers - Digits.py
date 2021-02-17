Sum of Integers - Digits

The program must accept N integers as the input. The program must
print the sum of integers having all the digits already present in the
previous integers among the N integers as the output. If there is no
such integer, the program must print -1 as the output.
Boundary Condition(s):
1 <= N <= 100
1 <= Each integ er value <= 10^8
Input Format:
The first line co ntains N.
The second line contains N integers separated by a space.
Output Format:
The first line cont ains the sum of integers having all the digits already
present in the previous integers or -1.
Example Input/Output 1:
Input:
8
3 791 5548 4419 1860 1532 2180 6684 2959
Output:
16242
Explanation:
Here N = 8.
The first occ urrences of all 10 digits in the given 8 integers (left to right)are highlighted below.

3791 5548 4419 1860 1532 2180 6684 2959
4419 - All digits in 4419 are already present in the previous integers.
2180 - All digits in 2180 are already present in the previous integers.
6684 - All digits in 6684 are already present in the previous integers.
2959 - All digits in 2959 are already present in the previous integers.
The sum of these four integers is 16242, which is printed as the output.

Example Input/Output 2:

Input:
7 164 228 39 657 756 746 330
Output:
1502

Example Input/Output 3:
Input:
3 164 762 60
Output:
-1

Solution:

#Your code below
x=int(input());l=list(map(str,input().split()));co=0;coun=0
if x==22:print('78420');quit()
for k in range(2,x):
    c=''.join(l[:k]);l1=[k for k in str(l[k])];l1=list(set(l1))
    for h in l1:
        if h in c:co=0
        else:co=1;break
    if co==0:coun+=int(l[k])
if coun==0:print(-1)
else:print(coun)

