from typing import List
class Solution:
    def move_zeros(self,nums:List)->None:
        zeros = []
        pos = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[pos] = nums[i]
                pos+=1
        for i in range(pos,len(nums)):
            nums[i]=0


if __name__ == "__main__":
    sol = Solution()
    nums = [121,5,4,0,0,34]
    sol.move_zeros(nums)
    print(nums)
