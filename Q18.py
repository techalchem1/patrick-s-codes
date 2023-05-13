string_list = input("Enter a list of strings: ").split()
vowels = 'aeiou'
new_list = []
for s in string_list:
    new_string = ''
    for char in s:
        if char.lower() in vowels:
            new_string += '*'
        else:
            new_string += char
    new_list.append(new_string)
print(new_list)