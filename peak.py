def find_peak(nums):
    if len(nums)<=0:
        return -1
    
    start = 0
    end = len(nums)-1    

    while start<end:
        mid = (start + end)//2
        if nums[mid]<nums[mid+1]:
            start = mid+1
        else:
            end = mid
    return start

nums = [1,2,3,1,2,1]
print(find_peak(nums))

