# Rearrange the array so that result[i] = i when i exists in the array

arr = list(map(int, input("Enter array elements: ").split()))

result = [-1] * len(arr)

for i in range(len(arr)):
    if i in arr:
        result[i] = i

print("Modified array:", result)
