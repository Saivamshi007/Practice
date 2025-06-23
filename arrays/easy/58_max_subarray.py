from typing import List
class Solution:
    def max_sub_array(self,nums:List[int])->int:
        max_sum = float('-inf')
        i,j = 0,len(nums)
        max_sum = float("-inf")


        while i<j:
            sub = sum(nums[i:j])
            max_sum = max(max_sum,sub)
            if max_sum>sub:
                i+=1
            else:
                j-=1


                
        return max_sum 
    
if __name__ == "__main__":
    nums = [5,4,-1,7,8]
    sol = Solution()
    print(sol.max_sub_array(nums))
