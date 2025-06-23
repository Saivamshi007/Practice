from typing import List
class Solution():
    def running_sum(self,nums:List)->None:
        n = len(nums)

        for i in range(1,n):
          
            nums[i]+=nums[i-1]
    


if __name__=="__main__":
    sol = Solution()
    nums = [1,2,3,4]
    sol.running_sum(nums)
    print(nums)