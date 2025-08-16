n = int(input())
count = 0
temp = n
while temp > 0:
    count += temp & 1
    temp >>= 1
print(count)  