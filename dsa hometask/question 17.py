"""Q17:
Reverse the array using Single Pointer"""
arr=[1,2,3,4,5]
n = len(arr)

for i in range(n // 2):
    j = n - 1 - i

    arr[i], arr[j] = arr[j], arr[i]
print(arr)