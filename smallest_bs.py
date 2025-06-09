def find_first(nums,target):
    start =0
    end = len(nums)-1
    result = -1
    while start <= end:
        mid = (start+end)//2
        if nums[mid]>target:
            result = mid
            end = mid-1
        else:
            start = mid+1
    if result == -1:
        return-1
    else:
        return nums[result]

            
        
    
       
        

nums = [1, 3, 5, 7, 9]
target = 7
print(find_first(nums,target))

