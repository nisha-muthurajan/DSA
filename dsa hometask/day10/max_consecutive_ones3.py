"""class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
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
        return maximum"""

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