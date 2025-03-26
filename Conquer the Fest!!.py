'''Conquer the Fest!!
IIIT Pune is celebrating its annual fest with a lineup of exciting events. And among the technical events InfInITy stands out as a prestigious coding contest, known for its challenging coding problems.

This year, the contest includes a difficult problem.
The problem has a difficulty level of 
B
B, and a participant needs an IQ of at least 
10
×
B
10×B to solve it.

You have an IQ of 
N
N. Can you take on the challenge and solve this tough problem, or is it too hard to crack?

Input Format
The first and only line of input will contain two space-separated integers 
N
N and 
B
B — your IQ, and the difficulty level of the problem you are trying to solve.
Output Format
Output on a single line the answer: "YES" (without quotes) if you can solve the problem, and "NO" (without quotes) otherwise.

Each character of the output may be printed in either uppercase or lowercase, i.e. if the answer is No, then all of NO, No, nO, and no will be accepted.

Constraints
1
≤
N
≤
500
1≤N≤500
1
≤
B
≤
100
1≤B≤100
Sample 1:
Input
Output
120 12
YES
Explanation:
The problem requires 
12
×
10
=
120
12×10=120 IQ, which you have exactly, so you can solve it.

Sample 2:
Input
Output
40 5
NO
Explanation:
The problem requires 
5
×
10
=
50
5×10=50 IQ, but you only have 
40
40, which is insufficient.

accepted
Accepted
22540
total-Submissions
Submissions
37612
accuracy
Accuracy
67.58
Did you like the problem statement?
15 users found this helpful
More Info
Time limit1 secs
Memory limit1.5 GB
Source Limit50000 Bytes'''

a,b= map(int,input().split())
c=b*10
if a>=c:
    print("YES")
else:
    print("NO")
