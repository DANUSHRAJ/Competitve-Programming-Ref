String Matching Points

The program must accept a string S and N string values as the input.
The program must calculate the sum of string matching points based
on the following conditions.
- If a 2-letter word is formed using the string S, then it has 1 point.
- If a 3-letter word is formed using the string S, then it has 2 points .
- If a 4-letter word is formed using the string S, then it has 3 points.
- If a 5-letter word is formed using the string S, then it has 4 points.
- If a 6-letter word is formed using the string S, then it has 5 points.
- If a word is exactly equal to the string S, then it has 10 bonus poin ts.
- For all other words that cannot be formed using the string S, 0 point s.
Finally, the program must print the total points for the given N words
as the output.
Boundary Condition(s):
1 <= N <= 100
1 <= Length of each string, S <= 6
Input Format:
The first line co ntains S.
The second line contain s N.
The next N lines, each conta ins a string value.
Output Format:
The first line cont ains the total points for the given N words
Example Input/Output 1:
Input:
apple
5
app
leap
people
pale
at
Output:
8
Explanation:
The string S = apple.
The 1 word "app" is a 3-letter word, which is formed using S.
So 2 points.
The 2 word "leap" is a 4-letter word, which is formed using S.
So 3 points.
The 3 word "people" is a 6-letter word, which is not formed using S.
So 0 points.
The 4 word "pale" is a 4-letter word, which is formed using S.
So 3 points.
The 5 word "at" is a 2-letter word, which is not formed using S.
So 0 points.
The total matching points is 8 (2 + 3 + 0 + 3 + 0).
So 8 is printed as the output.
Example Input/Output 2:
Input:
dot
4
to
do
dot
ttd
Output:
14


SOLUTION:

x=input().strip();co=0;t=0;l1=[]
for k in range(int(input())):
    co=0
    d=input().strip();b=[m for m in x]
    for h in d:
        if h in b:b.remove(h);t=1
        else:t=0;break
    if d==x:co+=10
    if t==1:
        if len(d)==2:co+=1;
        elif len(d)==3:co+=2;
        elif len(d)==4:co+=3;
        elif len(d)==5:co+=4;
        elif len(d)==6:co+=5;
    l1.append(co)
print(sum(l1))