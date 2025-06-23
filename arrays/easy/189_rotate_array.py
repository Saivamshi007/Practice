from typing import List
class Solution:
    def rotate_array(self,nums:List[int],k)->None:

        n = len(nums)
        k = k%n
        result = [0] * n

        for i in  range(n):
            result[(i+k)%n] = nums[i]

        for i in range(n):
            nums[i] = result[i]
    
        


        

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4,5,6,7] 
    k = 3
    sol.rotate_array(nums,k)
    print(nums)
