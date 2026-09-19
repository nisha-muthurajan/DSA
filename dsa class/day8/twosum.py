"""You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]."""

nums=list(map(int,input().split()))
target=int(input())
seen={}  #{value : index}
for i in range(len(nums)):
    wanted=target-nums[i]

    if wanted in seen:
        print(seen[wanted],i)
        break
    seen[nums[i]]=i
print("The target is not found")