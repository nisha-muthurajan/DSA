# first_last_occurrence.py

arr = list(map(int, input("Enter array elements: ").split()))
target = int(input("Enter the element: "))

first = -1
last = -1

for i in range(len(arr)):
    if arr[i] == target:
        if first == -1:
            first = i
        last = i

print("First occurrence:", first)
print("Last occurrence:", last)