Previous Alphabet Shift Encryption
The program must accept a string S as the input. The program must
encrypt the given string based on the following conditions.
- The first occurring alphabet in S always remains the same.
- All subsequent alphabets must be shifted by the alphabeti cal position
of the previous alphabet.
- If a character is not an a lphabet, then the program must keep the
character as it is.
Finally, the progr am must print the encrypted string as the output.
Note: The English alphabet set must be considered in a circular fas hion
when shifting alphabets.
Boundary Condition(s):
1 <= Length of S <= 100 0
Input Format:
The first line co ntains S.
Output Format:
The first line cont ains the encrypted string.
Example Input/Output 1:
Input:
hel#12 1#LO
Output:
hmq#121#XA
Explanation:
Here S = hel#121#LO.
1 character h -> It remains the same (as it is the first occurring
alphabet).
2 character e -> The alphabetical position of the previous alphabet h
= 8. So e becomes m (e + 8).
3 character l -> The alphabetical position of the previous alphabet e =
5. So l becomes q (l + 5).
4 character # -> It remains the same.
5 character 1 -> It remains the same.
6 character 2 -> It remains the same.
7 character 1 -> It remains the same.
8 character # -> It remains the same.
9 character L -> The alphabetical position of the previous alphabet l =
12. So L becomes X (L + 12).
10 character O -> The alphabetical position of the previous alphabet L
= 12. So O becomes A (O + 12).
The encrypted string is hmq#121#XA, which is printed as the output.
Example Input/Output 2:
Input:
1#2@3chO*cO#Cook#IE72
Output:
1#2@3ckW*rR#Rrdz#TN72


SOLUTION:

soni=input().strip();aki="";alp=[];alpl="abcdefghijklmnopqrstuvwxyz"
for x in soni:
    if x.isalpha():
        if len(alp)==0:alp+=[x];aki+=x 
        else:
            a=alpl.index(alp[-1].lower())+1;alp+=[x]
            new=alpl[(alpl.index(x.lower())+a)%len(alpl)]
            new=new if x.islower() else new.upper();aki+=new
    else:aki+=x
print(aki