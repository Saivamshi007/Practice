from typing import List
class Solution:
    def pemutate(self,nums:List[int])-> List:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans

if __name__ == "__main__":
    sol = Solution()
    nums = [0,2,1,5,3,4]
    print(sol.pemutate(nums))
    