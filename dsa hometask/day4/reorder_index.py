"""Q15:
Given two integer arrays of the same length, arr[] and index[], the task is to reorder the elements in arr[] such that after reordering, each element from arr[i] moves to the position index[i]. The new arrangement reflects the values being placed at their target indices, as described by index[] array.
Example: 
Input: arr[] = [10, 11, 12], index[] = [1, 0, 2]
Output: 11 10 12
Explanation: 10 moves to position 1, 11 to 0, and 12 stays at 2.
Input: arr[] = [1, 2, 3, 4], index[] = [3, 2, 0, 1]
Output: 3 4 2 1
Explanation: 1 moves to 3, 2 to 2, 3 to 0, 4 to 1.
Input: arr[] = [50, 40, 70, 60, 90], index[] = [3,  0,  4,  1,  2]
Output: 40 60 90 50 70"""
arr = [10, 11, 12]
index = [1, 0, 2]

n = len(arr)

result = [0] * n

for i in range(n):
    result[index[i]] = arr[i]

print(*result)