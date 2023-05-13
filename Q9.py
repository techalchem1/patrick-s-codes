num_list = input("Enter a list of integers separated by spaces: ").split()
num_list = [int(num) for num in num_list]
num_list.sort(reverse=True)
print("Sorted list: ", num_list)