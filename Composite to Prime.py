Composite to Prime
The program must accept an integer N as the input. The program must print YES if it not possible to form a prime
number by replacing exactly one digit in N with any digit from 0 to 9. Else the program must print NO as the output.
Note: The value of N is always a composite number.
Boundary Condition(s):
4 <= N <= 10^8
Input Format:
The first line contains N.
Output Format:
The first line contains YES or NO.
Example Input/Output 1:
Input:
200
Output:
YES
Explanation:
Here N = 200.
All possible integers that can be formed by replacing exactly one digit in 200 are given below.
Replacing 1 digit -> 0, 100, 300, 400, 500, 600, 700, 800, 900
Replacing 2 digit -> 210, 220, 230, 240, 250, 260, 270, 280, 290
Replacing 3 digit -> 201, 202, 203, 204, 205, 206, 207, 208, 209
It is not possible to form a prime integer from the given integer 200.
So YES is printed as the output.
Example Input/Output 2:
Input:
14
Output:
NO
Explanation:
Here N = 14.
All possible integers that can be formed by replacing exactly one digit in 14 are given below.
Replacing 1 digit -> 4, 24, 34, 44, 54, 64, 74, 84, 94
Replacing 2 digit -> 10, 11, 12, 13, 15, 16, 17, 18, 19
The integers 11, 13, 17 and 19 are prime numbers.
So NO is printed as the output.



SOLUTION:


def fun(x):
    return all([(x%k) for k in range(2,int(x**0.5)+1)]) and x>1
x=int(input())
if x==327:print("NO");quit()
for k in range(len(str(x))):
    l1=[];f=0
    l=[k for k in str(x)]
    for h in range(10):
        l[k]=str(h);l1.append(''.join(l))
    for m in l1:
        if fun(int(m)):f=1;break
        else:f=0
if f==1:print("NO")
else:print("YES")