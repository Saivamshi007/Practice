from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        left,right = 0,n-1
        for i in range(n-1,-1,-1):
            left_val = nums[left]**2
            right_val = nums[right]**2
            if left_val < right_val:
                result[i] = right_val
                right-=1
            else:
                result[i] = left_val
                left+=1
        return result

if __name__ == '__main__':
    s = Solution()
    nums = [-7,-3,2,3,11]
    print(s.sortedSquares(nums))