# Question: Calculate the prefix sum of an array.
inp = [8, 20, 12, 40]
# out: [8, 28, 40, 80]
total = []
count = 0
for i in inp:
    count += i
    total.append(count)

print(total)



