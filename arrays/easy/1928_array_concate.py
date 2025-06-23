from typing import List
class Solution:
    def concate(self,nums:List[int])->List:
        ans = nums.copy()
        ans.extend(nums)
        return ans

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3]
    print(sol.concate(nums))
