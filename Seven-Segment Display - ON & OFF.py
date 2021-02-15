
Seven-Segment Display - ON & OFF

In a seven-segment display (an electronic display consists of 7 LEDs),
the digits change after each second. Each segment in the display has a
name. The names of the seven segments are given below.
Top segment - a
Top-right segme nt - b
Bottom-right segment - c
Bottom segment - d
Bottom-left segment - e
Top-left segment - f
Middle segment - g
The program must a ccept a string S containing only digits as the input.
The digits in the string S represent the digits displayed using the sevensegment
LED. Initially, all 7 segments are OFF. For each transition of
one digit to the next, the program must print the names of the
segments that change state (ON -> OFF or OFF -> ON) as the output.
After displaying all the given digits, the 7 segments will become OFF. If
no segment has changed in a transition, the program must print -1 for
that transition.
Boundary Condition(s):
1 <= Length of S <= 100
Input Format:
The first line co ntains S.
Output Format:
The first X+1 lines (where X represents the length of S), each containing
the names of the segments that change state or -1.

Example Input/Output 1:

Input:
24110

Output:
a b d e g
a c d e f
f g
-1
a d e f
a b c d e f

Explanation:
Initially, all 7 segments are OFF.
1 transition (OFF -> 2): The segments a, b, d, e and g get the change.
2 transition (2 -> 4): The segments a, c, d, e and f get the change.
3 transition (4 -> 1): The segments f and g get the change.
4 transition (1 -> 1): No change.
5 transition (1 -> 0): The segments a, d, e and f get the change.
6 transition (0 -> OFF): The segments a, b, c, d, e and f get the
change.

Example Input/Output 2:

Input:
8537

Output:
a b c d e f g
b e
b f
d g
a b c





SOLUTION:

d = {0:['a', 'b', 'c', 'd', 'e', 'f'], 1:['b', 'c'], 2:['a', 'b', 'g', 'e', 'd'], 3:['a', 'b', 'g', 'c', 'd'], 4:['b', 'c', 'g', 'f'], 5:['a', 'f', 'g', 'c', 'd'], 6:['a', 'c', 'd', 'e', 'f', 'g'], 7:['a', 'b', 'c'], 8:['a', 'b', 'c', 'd', 'e', 'f', 'g'],9:['a', 'b', 'c', 'd','f', 'g']}
s = input().strip()
print(' '.join(sorted(d[int(s[0])])))
for i in range(1, len(s)):
    if s[i - 1] == s[i]:
        print(-1)
    else:
        t = d[int(s[i - 1])] + d[int(s[i])]
        se = sorted([i for i in t if t.count(i) == 1])
        print(*se)
print(*sorted(d[int(s[-1])]))