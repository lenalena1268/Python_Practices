s = input("Enter a String:")
k = input("Enter the letter:")
a = []
for i in range(len(s)):
    if k in s[i]:
        a = i

print(a)