length = int(input("Enter lenth:"))
num = []
for i in range(length):
    n=int(input("Enter elements:"))
    num.append(n)

if len(num)%2 != 0:
    mid = (len(num)+1)//2

else:
    mid = len(num)//2

half_arr = num[:mid]
print(half_arr)