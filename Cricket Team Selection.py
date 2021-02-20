Cricket Team Selection

There are two cricket teams with 6 players in each team to play world
super six league. The program must accept the names N and the
batting average A of 12 players (6 in each team) as the input. The
selection committee decided to merge the two teams into a single
team with 6 players by eliminating the players with the least batting
average among the 12 players from the two teams. Then the players in
the selected team must be sorted in descending order based on their
batting average. Finally, the program must print the name and the
batting average of all the players in the selected team as the output.
Note: The batting average of all 12 players are always unique.
Boundary Condition(s):
1 <= Length of each play er's name <= 20
2 <= A <= 75
Input Format:
The first six line s, each containing the names of the players and their
batting average of the first team.
The next six lines, each containing the names of the players and their
batting average of the second team.
Output Format:
The first six lines, each containing the names of the players and their
batting average of the selected team.Example Input/Output 1:
Input:
Kohli 59.3
Dhawan 45.1
Prithvi 28.0
Rahane 35.3
Rahul 47.6
Manish 35.1
Shreyas 49.9
Rishabh 26.7
Hardik 29.9
Jadeja 31.9
Bumrah 3.8
Bhuvneshwar 14.2
Output:
Kohli 59.3
Shreyas 49.9
Rahul 47.6
Dhawan 45.1
Rahane 35.3
Manish 35.1
Explanation:
After eliminating the 6 players with the least batting average, the
players in both the teams are given below.
The players from the first team are Kohli, Dhawan, Rahane,
Rahul and Manish.
A player from the second team is Shreyas.
After sorting the players in the selected team based on the batting
average in descending order, the names of the players and their batting
average in the selected team are given below.
Kohli 59.3
Shreyas 49.9
Rahul 47.6
Dhawan 45.1
Rahane 35.3
Manish 35.1

Example Input/Output 2:

Input:
Finch 41.0
Jason 9.5
Carey 34.2
Ashton 21
Cummins 9.6
Handscomb 33.3
Josh 13.2
Marnus 50.8
Kane 15.9
Smith 42.5
Turner 35.5
Warner 45.8

Output:
Marnus 50.8
Warner 45.8
Smith 42.5
Finch 41.0
Turner 35.5
Carey 34.2


SOLUTION

l=[]
for k in range(12):x=input().split(' ');l.append([x[0],float(x[-1])])
l.sort(key=lambda x:x[1],reverse=1);l=l[:6]
for k in l:print(*k)