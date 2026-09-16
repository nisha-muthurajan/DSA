"""You are given two integer arrays nums1 and nums2 of sizes n and m, respectively. Calculate the following values:

answer1 : the number of indices i such that nums1[i] exists in nums2.
answer2 : the number of indices i such that nums2[i] exists in nums1.
Return [answer1,answer2].

 

Example 1:

Input: nums1 = [2,3,2], nums2 = [1,2]

Output: [2,1]"""


nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))

count1,count2=0,0
for i in nums1:
    if i in nums2:
        count1+=1
for j in nums2:
    if j in nums1:
        count2+=1
res=count1,count2
print(res)