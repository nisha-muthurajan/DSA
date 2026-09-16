# Reverse an array using two pointers

arr = list(map(int, input("Enter array elements: ").split()))

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print("Reversed array:", arr)
