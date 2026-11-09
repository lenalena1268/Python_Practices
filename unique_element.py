# Check if all elements are unique.
# inp = [4,6,2,8,9]
# out: True

inp =[9,4,3,3,7,7]
# out: False
unique = {}
for i in inp:
    if i not in unique:
        unique[i] = 1
    else:
        unique[i] += 1
        print(False)
        break

else:
    print(True)


        
    