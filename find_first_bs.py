def find_first(nums,target):
    start =0
    end = len(nums)-1
    result = -1
    while start <= end:
        mid = (start+end)//2
        if nums[mid]<target:
            start = mid+1
        else:
            result = mid
            end = mid-1
    return result

nums = [1, 3, 3, 3, 5, 7, 9]
target = 3
print(find_first(nums,target))

