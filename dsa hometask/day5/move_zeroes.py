# Move all zeroes to the end while preserving nonzero element order

nums = list(map(int, input("Enter array elements: ").split()))
k = 0

for i in range(len(nums)):
    if nums[i] != 0:
        nums[k] = nums[i]
        k += 1

while k < len(nums):
    nums[k] = 0
    k += 1

print("Array after moving zeroes:", nums)
