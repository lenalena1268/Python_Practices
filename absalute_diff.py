# Find two numbers that have the smallest absolute difference.
inp = [4,9,6,1]
# out: [4,6]

min_diff = 50
for i in range(len(inp)):
    for j in range(i+1,len(inp)):
        if inp[i] > inp[j]:
            diff = inp[i]-inp[j]
        else:
            diff = inp[j] - inp[i]

        if diff < min_diff:
            min_diff = diff
            result = [inp[i],inp[j]]
print(result)
