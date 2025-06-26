from typing import List
class Solution:
    def max_sub_array(self,nums:List[int])->int:
        max_sum = sub = nums[0]
        for i in range(1,len(nums)):
            sub = max(nums[i],sub+nums[i])
            max_sum = max(max_sum,sub)


                
        return max_sum 
    
if __name__ == "__main__":
    nums = [-2,-1]
    sol = Solution()
    print(sol.max_sub_array(nums))
