#  Check if a given list contains only numbers.

# Inp: ["7", "0", "python", "6", "sql"]
# out: False

# Inp: ["7", "5", "2", "8"]
# out: True


# inp = ["7", "5", "2", "8"]
inp = ["7", "0", "python", "6", "sql"]
a = "0123456789"
for i in inp:
    if i not in a:
        print(False)
        break
else:
    print(True)