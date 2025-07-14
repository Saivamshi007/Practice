from typing import List
class Solution:
    def TwoSum(self,nums:List,target:int)->List:
        seen = {}
        n = len(nums)
        for idx,num in enumerate(nums):
            sec = target - num
            if sec in seen:
                return [seen[sec],idx]
            seen[num] = idx
if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,2,5]
    print(sol.TwoSum(nums,5))