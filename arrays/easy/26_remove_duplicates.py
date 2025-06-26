from typing import List
class Solution:
    def removeDuplicates(self,nums:List)->int:
        pos = 1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[pos] = nums[i]
                pos+=1
            



if __name__ == "__main__":
    sol = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    sol.removeDuplicates(nums)
    