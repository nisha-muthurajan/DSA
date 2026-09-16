# Rearrange an array with O(1) extra space
# Every value must be an index from 0 to len(arr) - 1.

arr = list(map(int, input("Enter array elements: ").split()))
n = len(arr)

if any(value < 0 or value >= n for value in arr):
    print("Each element must be between 0 and", n - 1)
else:
    for i in range(n):
        arr[i] = arr[i] + (arr[arr[i]] % n) * n

    for i in range(n):
        arr[i] = arr[i] // n

    print("Rearranged array:", arr)
