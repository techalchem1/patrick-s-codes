string_list = input("Enter a list of strings: ").split()
reversed_list = []
for s in string_list:
    reversed_list.append(s[::-1])
print(reversed_list)