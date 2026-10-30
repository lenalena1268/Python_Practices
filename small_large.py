nums = [5,8,3,9,2,10]
largest = nums[0]
smallest = nums[0]
for n in nums:
    if n < nums[0] :
        smallest = n
    if n > nums[0]:
        largest = n

diff = largest  - smallest 
print(diff)