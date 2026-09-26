"""*Max Consecutive Ones II*
Problem Scenario: *Network Signal Stabilization*
A communication system records the status of a network connection for N consecutive time intervals.
•	1 represents a stable/active connection. 
•	0 represents a temporary connection failure. 
The system can recover at most one failed interval by treating one 0 as 1.
Your task is to find the maximum number of consecutive active intervals that can be obtained after recovering at most one failure.
Input Format
•	First line: An integer N, the number of intervals. 
•	Second line: N space-separated integers containing only 0 and 1. 
Output Format
Print a single integer representing the maximum number of consecutive 1s possible after changing at most one 0 into 1.
Constraints
•	1 ≤ N ≤ 100000 
•	Each element is either 0 or 1. 
•	At most one 0 can be changed to 1. 
Example
Input
7
1 0 1 1 0 1 1
Output
4
Explanation:
Change the second 0:
1 0 1 1 0 1 1
      ↓
1 0 1 1 1 1 1
The longest consecutive sequence is 5 actually, so the correct output for this example is:
5
The corresponding window is:
1 1 0 1 1 1
with only one zero.
________________________________________
5 Sample Test Cases
Test Case 1 — One zero in the middle
Input
7
1 0 1 1 0 1 1
Output
5
Explanation:
Choose the window 1 1 0 1 1 1 and convert the single 0 to 1.
________________________________________
Test Case 2 — Zero at the beginning
Input
6
0 1 1 1 1 1
Output
6
Explanation:
Convert the first 0 to 1.
________________________________________
Test Case 3 — Zero at the end
Input
6
1 1 1 1 1 0
Output
6
Explanation:
Convert the final 0 to 1.
________________________________________
Test Case 4 — Multiple zeros
Input
10
1 1 0 0 1 1 1 0 1 1
Output
5
Explanation:
The best window is:
1 1 0 0 1 1 1
but it contains two zeros, so it is invalid.
Instead, consider:
0 1 1 1 0 1
which has only one zero and gives 5 consecutive ones after flipping it.
________________________________________
Test Case 5 — All ones
Input
8
1 1 1 1 1 1 1 1
Output
8
Explanation:
There is no zero to flip, but all elements are already 1."""

n=int(input())
nums=list(map(int,input().split()))
maximum=0
zero_count=0
left=0
for right in range(n):
    if nums[right]==0:
        zero_count+=1
    while zero_count>1:
        if nums[left]==0:
            zero_count-=1
        left+=1

    maximum=max(maximum,right-left+1)
print(maximum)