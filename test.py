from typing import List
from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        col = dict(Counter(nums))
        for key,value in col.items():
            if value != 1:
                return key
        
                
        

if __name__ == "__main__":
    sol = Solution()
    nums1 = [1,2,3,3]
    sol.findDuplicate(nums1)
   