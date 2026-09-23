# cook your dish here
"""Q21:
Delete First Occurrence of Given Element from an Array
Given an array of integers, the task is to delete a given element from the array. If there are multiple occurrences of the element, we need to remove only its first occurrence.
Examples:
Input: arr[] = [10, 20, 30, 40], ele = 20
Output: [10, 30, 40]
Input: arr[] = [10, 20, 30, 40], ele = 25
Output: [10, 20, 30, 40]
Input: arr[] = [10, 20, 40, 20, 20 30], ele = 20
Output: [10, 40, 20, 20, 30]"""

arr=list(map(int,input().split()))
t=int(input())
n=len(arr)
for i in range(len(arr)):
    if t==arr[i]:
        for j in range(i,len(arr)-1):
            arr[j]=arr[j+1]
        n=n-1
        break
        
    
print(arr[:n])