num_list = []
div_sum = 0
for i in range(6):
    num = int(input("Enter an integer: "))
    num_list.append(num)
    if num % 3 == 0:
        div_sum += num
print("Sum of integers divisible by 3:", div_sum)