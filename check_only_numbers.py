#  Check if a given list contains only numbers.

# Inp: ["7", "0", "python", "6", "sql"]
# out: False

# Inp: ["7", "5", "2", "8"]
# out: True


# inp = ["7", "5", "2", "8"]
inp = ["7", "0", "python", "6", "sql"]
try:
    for i in inp:
        int(i)
    print(True)
except ValueError:
    print(False)