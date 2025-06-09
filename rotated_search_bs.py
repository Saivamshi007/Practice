def search_rotated_array(nums):
    start = 0
    end = len(nums)-1
    while start<end:
        mid = (start+end)//2
        if nums[mid]>nums[end]:
            start = mid+1
        else:
            end = mid
    return nums[start]
nums = [3,4,5,1,2]
print(search_rotated_array(nums))
    
