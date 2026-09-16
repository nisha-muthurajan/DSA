# cook your dish here
"""Question:Given an attendance markerwhere 0 represents absent and 1 represents present.Find total number of absentees for the given data
2
0 1 1 0 0 1 1 0
1 1 1 
--------------------------
Output:
4 students are absent out of 8
No absentess"""
import math
n=int(input())

for i in range(n):
    attendance=list(map(int,input().split(" ")))
    if 0 not in attendance:
        print("No absentees")
        print("Attentance percentage:100%")
    else:
        count_ab=attendance.count(0)
        count_pr=attendance.count(1)
        percentage=(count_pr/len(attendance))*100
        print(count_ab,"student absent out of",len(attendance),"students")
        print("Attentance percentage:",math.ceil(percentage))
        