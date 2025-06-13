from typing import List
class Solution:
    def findmin(self,nums:List[int])->int:
        left,right = 0,len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[mid]>=nums[right]:
                left = mid+1
            else:
                right = mid  
        return nums[right]


if __name__ == "__main__":
    sol = Solution()
    nums = [11,13,15,17]

    print(sol.findmin(nums))

