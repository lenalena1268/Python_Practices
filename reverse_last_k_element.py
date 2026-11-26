# Second Question: Reverse the last k elements of an array
# inp: lis = [1, 2, 3, 4, 5, 6]
lis = [1, 2, 3, 4, 5, 6]
k = 3
# out: [1, 2, 3, 6, 5, 4]
a = lis[:k]
b = lis[k:][::-1]
for i in b:
    a.append(i)

print(a)


