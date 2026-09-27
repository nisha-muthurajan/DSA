"""Cumulative Sales

Problem Statement

A company records its daily sales for N consecutive days.

Your task is to create a new array called the cumulative sales array, where the value at each position represents the total sales from Day 1 up to that day.

For each day:

cumulative[i] = sales[0] + sales[1] + ... + sales[i]
Example

Given:

Sales = [100, 200, 150, 300]

The cumulative sales are:

Day 1 → 100
Day 2 → 100 + 200 = 300
Day 3 → 100 + 200 + 150 = 450
Day 4 → 100 + 200 + 150 + 300 = 750

Therefore:

[100, 300, 450, 750]
Input Format
N
sales[0] sales[1] ... sales[N-1]
Output Format

Print the cumulative sales array.

Constraints
1 ≤ N ≤ 100000
0 ≤ sales[i] ≤ 10^6

Input:
5
100 200 150 300 250

Output:
100 300 450 750 1000

Input:
6
100 0 200 0 300 0

Output:
100 100 300 300 600 600"""


n=int(input())
nums=list(map(int,input().split()))
ans=[]
total=0
for i in range(len(nums)):
    total+=nums[i]
    ans.append(total)
print(*ans)

#Time=O(n)
#Space=O(n)