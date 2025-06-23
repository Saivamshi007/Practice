from typing import List
class Solution:
    def shuffle(self,nums:List[int],k:int)->List:
        n = len(nums)
        ans = [0]*n
        left = nums[:k]

        right = nums[k:]
        i = j = 0
        for pos in range(n):
            if pos%2 == 0:
                ans[pos] = left[i]
                i+=1
            else:
                ans[pos] = right[j]
                j+=1
        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4,4,3,2,1]
    n = 4
    print(sol.shuffle(nums,n))
