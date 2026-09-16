# Find and remove the first occurrence by shifting elements left

arr = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter the element to remove: "))

first_index = -1

for i in range(len(arr)):
    if arr[i] == target:
        first_index = i
        break

if first_index == -1:
    print("Element not found")
else:
    for i in range(first_index, len(arr) - 1):
        arr[i] = arr[i + 1]

    arr.pop()
    print("Array after removing first occurrence:", arr)
