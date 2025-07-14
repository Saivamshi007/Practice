from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count=0
        for i in range(n):
            sub = []
            for j in range(i,n):
                sub.append(nums[j])
                if sum(sub) == k:
                    count+=1
        return count 


if __name__ == "__main__":
    sol = Solution()
    nums = [1,1,1]
    k =2
    print(sol.subarraySum(nums,k))