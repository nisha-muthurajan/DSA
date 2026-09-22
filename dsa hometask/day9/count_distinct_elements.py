"""Given an integer array arr[] and a number k. Find the count of distinct elements in every window of size k in the array.

Examples:

Input: arr[] = [1, 2, 1, 3, 4, 2, 3], k = 4
Output: [3, 4, 4, 3]
Explanation:
First window is [1, 2, 1, 3], count of distinct numbers is 3.
Second window is [2, 1, 3, 4] count of distinct numbers is 4.
Third window is [1, 3, 4, 2] count of distinct numbers is 4.
Fourth window is [3, 4, 2, 3] count of distinct numbers is 3."""


arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter window size: "))

n = len(arr)
freq = {}
res = []

# First window
for i in range(k):
    freq[arr[i]] = freq.get(arr[i], 0) + 1

res.append(len(freq))

# Slide the window
for i in range(k, n):

    # Remove outgoing element
    outgoing = arr[i - k]
    freq[outgoing] -= 1

    if freq[outgoing] == 0:
        del freq[outgoing]

    # Add incoming element
    incoming = arr[i]
    freq[incoming] = freq.get(incoming, 0) + 1

    res.append(len(freq))

print(res)

#time complexity=o(n)
#space complexity=o(n)