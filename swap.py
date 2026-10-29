nums = [4,8,2,6,7]
for i in range(len(nums)):
    if i == 0:
     temp = nums[i]
     nums[i]= nums[-1]
     nums[-1] = temp
     
print(nums) 