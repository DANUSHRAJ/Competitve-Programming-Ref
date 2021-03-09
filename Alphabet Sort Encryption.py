Alphabet Sort Encryption
The program must accept two string values S and K as the input. The
string K represents a key, which is used to encrypt the given string S.
The string K always contains unique lower case alphabets. The program
must encrypt the string S using the key K based on the following steps.
Step 1: Assign the integer values from 1 to K to the alphabets arranged
in the string K in sorted order.
Step 2: Then assign those K in teger values to the alphabets in S
repeatedly till the end of the string S.
Step 3: Rearrange the alphabets in th e string S based on the integers
assigned in sorted order. If two or more alphabets have the same
integer, then those alphabets must be arranged in the order of their
occurrence.
Finally, the p rogram must print the encrypted string as the output.
Boundary Condition(s):
1 <= Length of S <= 100 0
1 <= Length of K <= 26
Input Format:
The first line co ntains S.
The second line contain s K.
Output Format:
The first line cont ains the encrypted string.
Example Input/Output 1:
Input:
skillrack
code
Output:
slkialckr
Explanation:
Here S = skillrack and K = code.
Step 1: code -> 1 4 2 3
Step 2: skillrack -> 1 4 2 3 1 4 2 3 1
Step 3: skillrack -> slkialckr (1 1 1 2 2 3 3 4 4)
So slkialckr is printed as the output.
Example Input/Output 2:
Input:
Individualistically
quick
Output:
iaiydutlvlcIiiandsl
Explanation:
Here S = Individualistically and K = quick.
Step 1: quick -> 4 5 2 1 3
Step 2: Individualistically -> 4 5 2 1 3 4 5 2 1 3 4 5 2 1 3 4 5 2 1
Step 3: Individualistically -> iaiydutlvlcIiiandsl
So iaiydutlvlcIiiandsl is printed as the output.

SOLUTION:

string=input().strip()
encrypt=input().strip()
sor=sorted(encrypt)
arr=[]
for i in encrypt:
    arr.append(sor.index(i)+1)
alpha,index=[],0    
for i in string:
    if index<len(arr):
        alpha.append([i,arr[index]])
    else:
        index=0
        alpha.append([i,arr[index]])
    index+=1 
alpha=sorted(alpha, key=lambda rearrange:rearrange[1])
for i in alpha:
    print(i[0],end='')
