from typing import List
from math import abs
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        result =  nums[0] + nums[1] + nums[2]
        for i in range(n-2):
            while i==1 and nums[i] == nums[i-1]:
                continue
            left,right = i+1,n-1
            while left<right:
                sum = nums[i]+nums[left]+nums[right]
                if abs(target-sum) < abs(target-result):
                    result = sum
                if  sum == target :
                    return sum
                elif sum<target:
                    left+=1
                else:
                    right-=1
        return result



if __name__ == "__main__":
    sol = Solution()
    nums = [-1,2,1,-4]
    target = 1

    sol.threeSumClosest(nums,target)