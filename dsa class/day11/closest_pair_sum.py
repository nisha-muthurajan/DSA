n = int(input())
arr = list(map(int, input().split()))
k = int(input())

left = 0
right = n - 1

mini = float('inf')
ans = []

while left < right:
    total = arr[left] + arr[right]
    diff = abs(total - k)

    if diff < mini:
        mini = diff
        ans = [arr[left], arr[right]]

    if total > k:
        right -= 1
    elif total < k:
        left += 1
    else:
        break

print("Pair:", *ans)
print("Sum:", sum(ans))
print("Difference:", mini)