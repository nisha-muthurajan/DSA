"""Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined."""

nums=list(map(int,input().split()))
k=int(input())
maximum=0
left=0
zero_count=0
for right in range(len(nums)):
    if nums[right]==0:
        zero_count+=1

    while zero_count>k:
        if nums[left]==0:
            zero_count-=1
        left+=1

    maximum=max(maximum,right-left+1)
print(maximum)