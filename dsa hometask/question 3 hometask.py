"""First and Last Occurrence
Problem Statement
Given an array and a target value X, find the first and last position where X occurs.
Positions are 0-based.
If the target does not occur, print -1 -1.
Input Format
N X
A1 A2 ... AN
Output Format
first_position last_position"""
# cook your dish here
N,X=map(int,input().split())
arr=list(map(int,input().split()))
res=[]
for i in range(N):
    if arr[i]==X:
        res.append(i)
if res:
    print(res[0],res[-1])
else:
    print("-1 -1")
