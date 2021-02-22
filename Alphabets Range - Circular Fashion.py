Alphabets Range - Circular Fashion
The program must accept a string S containing only lower case
alphabets as the input. The program must print all the alphabets
between every two alphabets (both inclusive) in the string S as the
output. The English alphabet set is considered in a cyclic fashion to
print the alphabets from one alphabet to another.
Boundary Condition(s):
2 <= Length of S <= 100
Input Format:
The first line co ntains S.
Output Format:
The first line cont ains a string as per the given condition.
Example Input/Output 1:
Input:
aepd
Output:
abcdeef ghijklmnoppqrstuvwxyzabcd
Explanation:
Here S = aep d.
The alphabets b etween a to e are a b c d e (a and e are inclusive).
The alphabets between e to p are e f g h i j k l m n o p (e and p a re
inclusive).
The alpha bets between p to d are p q r s t u v w x y z a b c d (p and d
are inclusive).
So abcdeefgh ijklmnoppqrstuvwxyzabcd is printed as the output

Example Input/Output 2:
Input:
apple
Output:
abcdefghijklmnopppqrstuvwxyzabcdefghijkllmnopqrstuvwxyzabcde
Example Input/Output 3:
Input:
aabbaa
Output:
aabbbcdefghijklmnopqrstuvwxyzaa

SOLUTION:

#Your code below
def fun(a,b):
    while(b!=a):
        print(a,end='')
        a=chr(ord(a)+1)
        if ord(a)==ord('z')+1:a='a'
    print(a,end='')
x='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz';
for k in range(10):x+=x
y=input().strip();x=list(x)
for k in range(len(y)-1):
    i1=x.index(y[k]);i2=x.index(y[k+1]);#print(*x[i1:i2+1],sep='',end='');x[i1:i2]=''
    fun(y[k],y[k+1])