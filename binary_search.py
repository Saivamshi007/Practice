def binary_search(nums,target):
    start = 0 
    end = len(nums)-1

    while start<=end:
        mid = (start+end)//2

        if nums[mid]<target:
            start = mid+1
        elif nums[mid]>target:
            end = mid-1
        else:
            return mid
    return -1
    

nums = [1,2,3,5,6]
target = 1
print(binary_search(nums,target))