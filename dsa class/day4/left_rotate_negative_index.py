# Left rotate an array using negative indexing

arr = list(map(int, input("Enter array elements: ").split()))
steps = int(input("Enter number of left rotations: "))

if arr:
    steps %= len(arr)
    split_index = -(len(arr) - steps)
    arr = arr[split_index:] + arr[:split_index]

print("Left rotated array:", arr)
