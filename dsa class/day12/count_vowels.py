"""count the no f vowels and consonants in the given string 
the string will contain only alphabets
but it can have both uppercase and lower case"""

s=input()
s=s.lower()
vowels_count=0
con_count=0
for i in range(len(s)):
    if s[i].isalpha():
        if s[i] in "aeiuo":
            vowels_count+=1
        elif s[i] not in "aeiuo":
            con_count+=1
print(vowels_count)
print(con_count)

#Time=O(n)
#Space=O(1)