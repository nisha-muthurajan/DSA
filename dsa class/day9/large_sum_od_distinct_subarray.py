arr = list(map(int, input("Enter array: ").split()))
k = int(input("Enter k: "))

freq = {}
window_sum = 0
max_sum = 0

for i in range(len(arr)):

    # Add current element
    freq[arr[i]] = freq.get(arr[i], 0) + 1
    window_sum += arr[i]

    # Keep window size = k
    if i >= k:
        outgoing = arr[i - k]
        window_sum -= outgoing

        freq[outgoing] -= 1

        if freq[outgoing] == 0:
            del freq[outgoing]

    # Check if window has k distinct elements
    if i >= k - 1 and len(freq) == k:
        max_sum = max(max_sum, window_sum)

print(max_sum)