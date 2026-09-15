# cook your dish here
"""Question:Given an attendance markerwhere 0 represents absent and 1 represents present.Find total number of absentees for the given data
2
0 1 1 0 0 1 1 0
1 1 1 
--------------------------
Output:
4 students are absent out of 8
No absentess"""


no_of_testcases=int(input())
even_avg=0
odd_avg=0
for i in range(no_of_testcases):
  arr=list(map(int,input().split(" ")))
  
  even_arr=[]
  odd_arr=[]
  for j in arr:
      
      
      if j%2==0:
          even_arr.append(j)
        
      else:
          odd_arr.append(j)
         
  
  if len(even_arr)==0:
      even_avg=0
      odd_avg=sum(odd_arr)/len(odd_arr)
  elif len(odd_arr)==0:
      odd_avg=0
      even_avg=sum(even_arr)/len(even_arr)
  else:
      even_avg=sum(even_arr)/len(even_arr)
      odd_avg=sum(odd_arr)/len(odd_arr)
  print("T",i+1)
  print("Even:", f"{even_avg:.2f}")
  print("Odd:", f"{odd_avg:.2f}")
  
      
  
  


