Construction of New Buildings 
The program must accept a character of size R*C representing a city as the input. 
The matrix consists of asterisks and hyphens. Each asterisk represents a building and each hyphen represents a land. The government has planned to construct 
new buildings in the city based on the following condition. - If a land is present in one of the four corners (top-left, top-right, bottom-left and bottom-right) 
of a building, then a new building is allowed to construct on that land. The program must print the maximum number of new buildings that can be built based on the 
given conditions. Boundary Condition(s): 2 <= R, C <= 50 Input Format: The first line contains R and C separated by a space. 
The next R lines, each contains C characters separated by a space. Output Format: The first line contains the maximum number of new buildings that can be built.
 Example Input/Output 1: 
 Input: 
 5 6 
 - - * - * - 
 - * - - - * 
 * - - - - * 
 - * - - - *
 * * * * - - 
 Output: 10 
 Explanation: The 10 new buildings can be constructed as given below. # - * - * - - * - # # * * - # - # * # * # # # * * * * * # - 
 Each hash symbol in the above matrix represents
 a new building. So 10 is printed as the output.
 
 Example Input/Output 2: 
 Input: 
 3 3 
 - * - 
 * - * 
 - * - 
 Output: 0

SOLUTION:

#Your code below
def fun(r,c,l,R,C):
    if r>=0 and r<=R-1 and c>=0 and c<=C-1:
        if l[r][c]=='-':
            l[r][c]='#'
x,y=map(int,input().split());l=[input().split() for _ in range(x)];c=0
for k in range(x):
    for h in range(y):
        if l[k][h]=='*':
            fun(k+1,h+1,l,x,y)
            fun(k+1,h-1,l,x,y)
            fun(k-1,h-1,l,x,y)
            fun(k-1,h+1,l,x,y)
for k in l:
    c+=k.count('#')
print(c)