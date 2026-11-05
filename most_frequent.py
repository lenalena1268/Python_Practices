numbers = [10,7,4,8,9,4,7,7,10,1,7,1]
frequncy ={}
max_count = 0
for num in numbers:
    if num in frequncy:
        frequncy[num] += 1
    else:
        frequncy[num] = 1

    if frequncy[num] > max_count:
        max_count = frequncy[num]
        count = num


print(count)