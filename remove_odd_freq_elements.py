# Question: Remove elements that appear an odd number of times
nums=[]
l=int(input("Enter the length:"))
for i in range(l):
    e=int(input("Enter the Element:"))
    nums.append(e)
print(nums)
d={}
a=[]
for n in nums:
    if n not in d:
        d[n]=1
    else:
        d[n]+=1

for n in d:
    if d[n] % 2 == 0:
        a.append(n)
print(d)
print(a)
