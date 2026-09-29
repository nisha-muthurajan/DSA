"""Do the mathematical operations from the user input  without using buildin function 
Input: 25 + 25
Output: 50 """

input_data = input()

input_list = list(input_data)

nums_list = []
nums = ""

for i in input_list:
    if i == " ":
        if nums != "":
            nums_list.append(nums)
            nums = ""
    else:
        nums += i

if nums != "":
    nums_list.append(nums)

sums = int(nums_list[0])

for i in range(1, len(nums_list), 2):

    if nums_list[i] == "+":
        sums += int(nums_list[i+1])

    elif nums_list[i] == "-":
        sums -= int(nums_list[i+1])

    elif nums_list[i] == "*":
        sums *= int(nums_list[i+1])

    elif nums_list[i] == "/":
        sums /= int(nums_list[i+1])

print(sums)