# Rearrange a sorted array alternately with maximum and minimum values

arr = list(map(int, input("Enter array elements: ").split()))

arr.sort()
n = len(arr)
temp = [0] * n
left = 0
right = n - 1

for i in range(n):
    if i % 2 == 0:
        temp[i] = arr[right]
        right -= 1
    else:
        temp[i] = arr[left]
        left += 1

for i in range(n):
    arr[i] = temp[i]

print("Rearranged array:", arr)
