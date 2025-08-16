from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = 0
        start = 0
        n = len(nums)
        max_sum = float('-inf')
        if n==1:
            return nums[0]/k

        for end in range(n):
            window_sum+= nums[end]

            if end - start+1>k:
                window_sum-=nums[start]
                start+=1
            
            if end-start+1 == k:
                max_sum = max(max_sum,window_sum)
        return max_sum/k



if __name__ == "__main__":
    sol = Solution()
    nums = [1,12,-5,-6,50,3] 
    k=4
    print(sol.findMaxAverage(nums,k))