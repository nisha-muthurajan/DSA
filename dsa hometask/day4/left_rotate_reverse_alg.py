"""Q13:
Rotate the Array by left n times using Reverse Algorithm"""
arr = list(map(int, input().split()))
k = int(input())

n = len(arr)

k = k % n

# Reverse first k elements
arr[:k] = arr[:k][::-1]

# Reverse remaining elements
arr[k:] = arr[k:][::-1]

# Reverse entire array
arr[:] = arr[::-1]

print(arr)