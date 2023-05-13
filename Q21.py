list = ['banana', 'apple', 'pineapple']
sorted(list,key=lambda word: sum(ch in 'aeiou' for ch in word),
        reverse=True)
print(list)