string_list = ['Sleeples', 'nights', 'ahead', 'result ', 'to', 'success']
max_length = 0
for string in string_list:
    if len(string) > max_length:
        max_length = len(string)
print("The length of the longest string is:")
print(max_length)

#string_list = input("Enter a list of strings (comma-separated): ").split(",")
  #longest_string = max(string_list, key=len)
   #print("The longest string has length", len(longest_string))