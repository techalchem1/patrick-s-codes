num_list = input("Enter a list of integers separated by spaces: ").split()
max_num = int(num_list[0])
for num in num_list:
     if int(num) > max_num:
        max_num = int(num)
print("The largest integer is: ", max_num)