"""Q12:
Right Rotation (Clockwise) - n times
Consider index only from 0 to n-1"""
arr = list(map(int, input().split()))
k = int(input())

n = len(arr)

k = k % n

arr = arr[n-k:] + arr[:n-k]

print(arr)