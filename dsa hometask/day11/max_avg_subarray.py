"""You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75"""

nums=list(map(int,input().split()))
k=int(input())
ans = sum(nums[:k])
maxAvg = float(ans) / k

for i in range(1, len(nums) - k + 1):
    ans = ans - nums[i - 1] + nums[i + k - 1]
    maxAvg = max(maxAvg, float(ans) / k)
print(maxAvg)