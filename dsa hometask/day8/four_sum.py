
"""Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]"""


nums=list(map(int,input().split()))
target=int(input())
nums.sort()

result = []
n = len(nums)

for i in range(n - 3):

            # Skip duplicate first values
    if i > 0 and nums[i] == nums[i - 1]:
        continue

    for j in range(i + 1, n - 2):

                # Skip duplicate second values
        if j > i + 1 and nums[j] == nums[j - 1]:
            continue

        left = j + 1
        right = n - 1

        while left < right:

            total = (
                        nums[i]
                        + nums[j]
                        + nums[left]
                        + nums[right]
                    )

            if total == target:

                result.append([
                            nums[i],
                            nums[j],
                            nums[left],
                            nums[right]
                        ])

                left += 1
                right -= 1

                        # Skip duplicate left values
                while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        # Skip duplicate right values
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < target:
                left += 1

            else:
                right -= 1

print(result)
        