from operator import itemgetter
dict_to_be_sorted=[{'name': 'Nice Nice', 'age': '700'}, {'name': 'Collins', 'age': 19}, {'name': 'python', 'age': 32}]
newdict = sorted(dict_to_be_sorted, key=itemgetter('name'))
print(newdict)