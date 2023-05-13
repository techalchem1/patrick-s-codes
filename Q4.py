nums = []
for i in range(10):
    num = int(input("Enter a number: "))
    nums.append(num)    
sum = 0
for num in nums:
    sum += num   
print("The sum of the 10 numbers is:", sum)