String - Four Substrings
The program must accept a string S as the input. The length of the
string S is always a perfect square (X ). The program must divide the
string S into substrings based on the following conditions.
- The 1 substring must be formed using the first (X-1)*4 ch aracters.
- The 2 substring must be formed using the next (X-3)*4 characters .
- The 3 substring must be formed using the next (X-5)*4 characters.
- Similarly, the remaining substrings are formed using the remaining
characters in S.
- If X is odd, the n the last substring has only one character.
For each substring among the obtained substrings, the pro gram must
divide the substring into 4 substrings of equal length. Then the
program must print the 1 characters of all four substrings,
2 characters of all four substrings, 3 characters of all four substrings
and so on. If the last substring has only one character, then the
program must print the last substring as it is.
Boundary Condition(s):
4 <= Length of S <= 250 0
Input Format:
The first line co ntains S.
Output Format:
The first line cont ains a string value representing the characters of S
based on the given conditions.
Example Input/Output 1:
Input:
abcdefghijklmnopqrstuvwxz1234567890A
Output:
afkpbglqchmrdinsejotux25vz36w147890A
Explanation:
The length of S is 36, which is a perfect squre. So X = 6 (6*6 = 36).
1 substring -> abcdefghijklmnopqrst -> abcde fghij klmno pqrst
2 substring -> uvwxz1234567 -> uvw xz1 234 567
3 substring -> 890A -> 8 9 0 A
Hence the output is
afkpbglqchmrdinsejotux25vz36w147890A
Example Input/Output 2:
Input:
skillrack
Output:
silaklrck


solutIOn:

s=input().strip()
n=len(s)
x=int(n**0.5)
for i in range(1,x+1,2):
    t=s[:(x-i)*4]
    s=s[(x-i)*4:]
    m=''
    for j in range(x-i):
        for k in range(4):
            m+=t[k*(x-i)+j]
    print(m,end='')
print(s)