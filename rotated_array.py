def rotated_array(nums):
    start = 0
    end = len(nums)-1
    result= 0

    while start<end:
        mid = (start+end)//2
        if nums[mid]>nums[mid+1]:
            return nums[mid+1]
        elif nums[mid]<nums[mid+1]:
            start = mid+1
        else:
            end = mid -1
    return nums[0]

nums = [3,4,5,1,2]
print(rotated_array(nums))
