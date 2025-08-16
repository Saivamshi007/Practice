from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx,val in enumerate(nums):
            reminder = target - val
            if reminder in seen:
                return [seen[reminder],idx]
            seen[val] = idx          

if __name__ == "__main__":
    s = Solution()
    nums = [3,2,4]
    target = 6
    s.twoSum(nums,target)