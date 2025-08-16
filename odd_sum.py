n = int(input().strip())
nums = []
while len(nums)< n:
    nums+= list(map(int, input().strip().split()))

odd_sum = sum(x for x in nums if x % 2 != 0)
print(odd_sum) 