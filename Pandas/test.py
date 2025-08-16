nums = [1,2,3,4]
no_swaps = len(nums)//2
j=0
for i in range(0,no_swaps):
    nums[j],nums[j+1] = nums[j+1],nums[j]
    j+=2
print(nums)