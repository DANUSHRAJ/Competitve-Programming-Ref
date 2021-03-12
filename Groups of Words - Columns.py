Groups of Words - Columns
The program must accept a string S containing only lower case
alphabets and spaces as the input. All the words in the string S always
have the same length. The program must group the words starting with
the same alphabet. The groups must be sorted based on the first
alphabet and the words in each group must be sorted in the order of
their occurrence. Then the program must print the groups of words
column by column as shown in the Example Input/Output section. The
empty spaces must be printed as asterisks.
Boundary Condition(s):
3 <= Length of S <= 100 0
Input Format:
The first line co ntains S.
Output Format:
The lines, each co ntains a string value.
Example Input/Output 1:
Input:
eat cat mat egg man max car ear cow
Output:
cateatmat
careggman
cowearmax
Explanation:
Here the length of each word in the given string is 3.
After grouping the words starting with the same alphabet, the words
becomes
e - eat, egg, ear
c - cat, car, cow
m - mat, man, max
After sorting the groups based on the first alphabet, the words are
printed column by column as given below.
cateatmat
careggman
cowearmax
Example Input/Output 2:
Input:
blue live lady bulk band best task land term fire year fact turn tune
Output:
bluefirelivetaskyear
bulkfactladyterm****
band****landturn****
best********tune****

#Your code below
l=input().split();l1=[k[0] for k in l];l1=sorted(list(set(l1)));l2=[];le=len(l[0])
for k in l1:
    la=[]
    for h in l:
        if k==h[0]:la.append(h)
    l2.append(la)
#print(l2)
ma=len(max(l2,key=len))
#print(ma)
for k in l2:
    if len(k)<ma:
        for m in range(abs(len(k)-ma)):
            k.append('*'*le)
#print(l2)
for k in range(ma):
  for h in range(len(l2)):
    print(l2[h][k],end='')
  print()
