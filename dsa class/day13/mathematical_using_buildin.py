input_data = input()
nums_list = input_data.split()

sums = int(nums_list[0])

for i in range(1, len(nums_list), 2):

    operator = nums_list[i]
    num = int(nums_list[i+1])

    if operator == "+":
        sums += num

    elif operator == "-":
        sums -= num

    elif operator == "*":
        sums *= num

    elif operator == "/":
        sums /= num

print(sums)