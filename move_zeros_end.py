# Move all zeros to the end of the list without changing the order of other elements.
nums = [0, 5, 0, 8, 3, 0, 7]
# out =[5, 8, 3, 7, 0, 0, 0]

a = []
b = []
for i in range(len(nums)):
    if nums[i] !=0:
        a.append(nums[i])
    else:
        b.append(nums[i])
numbers = a + b
print(numbers)