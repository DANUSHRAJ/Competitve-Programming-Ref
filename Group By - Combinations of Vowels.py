Group By - Combinations of Vowels
The program must accept N string values as the input. The program
must group the string values based on the combinations of vowels (No
vowels, a, ae, aei, aeio, aeiou, aeiu, aeo, aeou, aeu, ai, aio, aiou, aiu, ao,
aou, au, e, ei, eio, eiou, eiu, eo, eou, eu, i, io, iou, iu, o, ou and u). The
program must print all possible combinations of the vowels followed by
the string values that belong to the combination as shown in the
Example Input/Output section. The combinations of vowels must be
printed in the above mentioned order. The string values that belong to
a combination must be printed in the order of their occurrence.
Boundary Condition(s):
1 <= N <= 100
1 <= Length of each string value <= 100
Input Format:
The first line co ntains N.
The next N lines, each co ntaining a string value.
Output Format:
The lines contain ing the all possible combinations of the vowels
followed by the string values that belong to the combination.
Example Input/Output 1:
Input:
11
rat
tennis
normal
eagle
winter
bottle
intel
atom
journey
escape
by
Output:
No vowels - by
a - rat
ae - eagle,escape
ao - normal,atom
ei - tennis,winter,intel
eo - bottle
eou - journey
Explanation:
The string by has no vowels, so it belongs to "No vowels".
The string rat has only one vowel a, so it belongs to the combination
"a".
The string values eagle and escape have 2 vowels a and e, so they
belong to the combination "ae".
The string values normal and atom have 2 vowels a and o, so they
belong to the combination "ao".
The string values tennis, winter and intel have 2 vowels e and i, so
they belong to the combination "ei".
The string bottle has 2 vowels e and o, so it belongs to the
combination "eo".
The string journey has 3 vowels e, o and u, so it belongs to the
combination "eou".
Example Input/Output 2:
Input:
3
GAME
Mask
TASK
Output:
a - Mask,TASK
ae - GAME


SOLUTION:

from collections import defaultdict
d=defaultdict(list)
t=[]
for _ in range(int(input())):
    s=input().strip()
    if any([i in 'aeiou' for i in set(s.lower())]):
        d[''.join(sorted(set([i for i in set(s.lower()) if i in 'aeiou'])))].append(s)
    else:
        t.append(s)
if t:
    print('No vowels -',','.join(t))
for i in sorted(d.keys()):
    print(i,'-',','.join(d[i]))