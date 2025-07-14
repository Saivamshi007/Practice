from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        
        window_avg = sum(nums[:k])/k
        max_avg = window_avg

        if n == k:
            return window_avg
        

        for i in range(n-k):
            window_avg = window_avg - nums[i]/k + nums[i+k]/k 
            max_avg = max(max_avg,window_avg)
        return max_avg



if __name__ == "__main__":
    sol = Solution()
    nums = [9,7,3,5,6,2,0,8,1,9]
    k=6
    print(sol.findMaxAverage(nums,k))