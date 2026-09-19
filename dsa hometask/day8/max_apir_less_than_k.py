"""You are given an array arr of size n and an integer k. Your task is to find a pair of integers in the array such that it follows two conditions:

The sum of the pair is the maximum possible but less than k.
Out of all such pairs, choose the one with the maximum absolute difference between the two integers.
If no such pair exists, return (-1, -1).

Example:

Input: arr = [2, 4, 3, 6, 8, 10], k = 10
Output: (3, 6)
Explanation:
The pair (3, 6) has a sum of 9, which is less than 10. Among all pairs with sums less than 10, (3, 6) has the maximum absolute difference."""

arr=list(map(int,input().split()))
k=int(input())
arr.sort()
    
left, right = 0, len(arr) - 1
best_sum = -1
best_diff = -1
ans = (-1, -1)
    
while left < right:
    s = arr[left] + arr[right]
    
    if s < k:
        diff = arr[right] - arr[left]
    
        if s > best_sum or (s == best_sum and diff > best_diff):
            best_sum = s
            best_diff = diff
            ans = (arr[left], arr[right])
    
        left += 1
    else:
        right -= 1
    
print(ans)