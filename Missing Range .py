Missing Range 

The program must accept N sorted (in ascending order) integers as the input. 
The program must print the missing range of values as the output. If none of the values are missing the program must print -1 as the output.
 Boundary Condition(s): 2 <= N <= 10^4 Input Format: The first line contains N. 
 The second line contains N integer values separated by a space. 
 Output Format: The first line contains -1 or the missing range of values separated by a space. 
 Example Input/Output 1: 
 Input: 5 1 2 5 6 12 
 Output: 3-4 7-11 
 Explanation: The missing values are 3,4. Hence the range is printed as 3-4. The next missing values are 7,8,9,10,11. Hence the range is printed as 7-11. 

Example Input/Output 2: 
Input: 6 1 2 3 5 6 7 
Output: 4-4 


Example Input/Output 3: 
Input: 7 1 2 3 4 5 6 7 
Output: -1




#Your code below
x=int(input());l=list(map(int,input().split()));a=[k for k in range(1,l[-1]+1)]
sr=1;l1=[]
for k in l:
    if k-sr!=0:
        l1.append(str(sr)+'-'+str(k-1))
    sr=k+1
if l1:print(*l1)
else:print(-1)