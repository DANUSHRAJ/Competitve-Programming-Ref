Swap Validation
The program must accept a string S and N string values as the input.
For each string among N string values, the program must compare it
with the given string S. If it is possible to form the string S by swapping
two characters exactly once, the program must print YES as the output.
Else the program must print NO as the output. The swapping must be
done when comparing the string values even if they are equal.
Note: The length of all string values are always equal.
Boundary Condition(s):
2 <= Length of S <= 100
1 <= N <= 50
Input Format:
The first line co ntains S.
The second line contain s N.
The next N lines, each conta ins a string value.
Output Format:
The first N lines, each contains YES or NO.
Example Input/Output 1:
Input:
ABCDE
4
BACDE
ABEDC
CDEAB
ARCDS
Output:
YES
YES
NO
NO
Explanation:
Here S = ABCDE and N = 4.
The 1 string is BACDE. After swapping the first two characters, the
string becomes ABCDE. So YES is printed.
The 2 string is ABEDC. After swapping the third and fifth characters,
the string becomes ABCDE. So YES is printed.
The 3 string is CDEAB. It is not possible to form ABCDE by swapping
the two characters exactly once. So NO is printed.
The 4 string is ARCDS. It is not possible to form ABCDE by swapping
the two characters exactly once. So NO is printed.
Example Input/Output 2:
Input:
123@456
3 623@451
1234@56
132@465
Output:
YES
YES
NO
Example Input/Output 3:
Input:
abcabc
1
abcabc
Output:
YES
Example Input/Output 4:
Input:
abcde
1
abcde
Output:
NO



SOLUTION:

s=input().strip()
for k in range(int(input())):
    t=input().strip()
    l=[]
    for i in range(len(t)):
        if s[i]!=t[i]:
            l.append(i)
    if (len(l)==0 and len(set(t))!=len(t)) or (len(l)==2 and s[l[0]]==t[l[1]] and s[l[1]]==t[l[0]]):
        print("YES")
    else:
        print("NO") 