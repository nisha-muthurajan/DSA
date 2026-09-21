"""Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.

Note: A subarray is a contiguous part of any given array.

Examples:

Input: arr[] = [100, 200, 300, 400], k = 2
Output: 700
Explanation: arr2 + arr3 = 700, which is maximum"""

arr=list(map(int,input().split()))
k=int(input())
n=len(arr)
window=sum(arr[0:k])
max_sum=window

for i in range(1,n-k+1):
    window-=arr[i-1]
    window+=arr[i+k-1]
    if window>max_sum:
        max_sum=window
print(max_sum)