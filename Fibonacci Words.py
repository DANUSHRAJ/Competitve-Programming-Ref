
Fibonacci Words
The program must accept an integer N as the input. The program must
print the first N Fibonacci words formed by repeating them in the same
way as generating Fibonacci numbers. The first term in the Fibonacci
words must be "a" and the second term in the Fibonacci words must be
"b".
Boundary Condition(s):
1 <= N <= 25
Input Format:
The first line co ntains N.
Output Format:
The first line cont ains the first N Fibonacci words.
Example Input/Output 1:
Input:
6
Output:
a b ba b ab babba babbabab
Explanation:
Here N = 6 a nd the first two terms in the Fibonacci words are "a" and
"b".
The 3 term in the Fibonacci words is ba ("b" + "a").
The 4 term in the Fibonacci words is bab ("ba" + "b ").
The 5 term in the Fibonacci words is babba ("bab" + " ba").
The 6 term in the Fibonacci words is babbabab ("babba" + "bab").
Hence the output is
a b ba bab babba ba bbabab
Example Input/Output 2:
Input:
9
Output:
a b ba bab babba babbabab babbababbabba
babbababbabbababbabab babbababbabbababbababbabbababbabba


SOLUTION:

#Your code below
from functools import reduce
n=int(input());
if n==1:print('a');quit()
fib=lambda x:reduce(lambda a , _: a+[a[-1]+a[-2]], range(n-2),['a','b'])
print(*fib(n))