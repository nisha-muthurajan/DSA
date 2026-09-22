"""Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

 

Example 1:

Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold)."""

arr=list(map(int,input().split()))
k=int(input())
threshold=int(input())
n=len(arr)
window=arr[:k]
total=sum(window)
count=0
if total/k >=threshold:
    count+=1
for i in range(1,n-k+1):
    total+=arr[i+k-1]-arr[i-1]
    if total/k >=threshold:
        count+=1
print(count)

#Time complexity=o(n)
#space complexity=o(n)