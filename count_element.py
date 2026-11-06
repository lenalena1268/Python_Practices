inp = [10,7,4,8,9,4,7,7,10,1,7,1]
count = {}
total = 0
for i in inp:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)

for i in count:
    if count[i] > 1:
        total += 1
print(total)