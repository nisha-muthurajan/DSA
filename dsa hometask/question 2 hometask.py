# cook your dish here
"""Problem: Placement Cutoff Count
A placement test is conducted for N candidates. Each candidate receives a score. A company has set a minimum cutoff score of C.
Your task is to count how many candidates scored at least C.
Note: A score exactly equal to C is also considered qualified.
Input Format
The first line contains two integers N and C. 
The second line contains N integers representing the candidates' scores. 
Output Format
Print a single integer representing the number of candidates who scored at least C.
Constraints
1 ≤ N ≤ 10⁵ 
0 ≤ score, C ≤ 100 
N scores will be provided. 
Sample Test Case 1
Input
6 60
45 72 61 58 90 60
Output
4
Explanation: Scores 72, 61, 90, 60 are at least 60."""
N,C=map(int,input().split())
arr=list(map(int,input().split()))
count=0
for i in arr:
    if i>=C:
        count+=1
print(count)