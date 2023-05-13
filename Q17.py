num_list = []
even_list = []
for i in range(10):
    num = int(input("Enter an integer: "))
    num_list.append(num)
    if num % 2 == 0:
        even_list.append(num)
print("List of even numbers:", even_list)