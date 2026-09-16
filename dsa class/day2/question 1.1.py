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
    
    count_ab=0
    count_pr=0
    atte=input()
    
    for i in atte:
      
      if i =="0":
          count_ab+=1
      elif i=="1":
          count_pr+=1
    
    percentage=(count_pr/(count_pr+count_ab))*100
    print(count_ab,"student absent out of",(count_pr+count_ab),"students") if count_ab>0 else print("No absentees")
    print(f"Attentance percentage:{math.ceil(percentage)}%")
        