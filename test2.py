from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        test = [i for i in range(1,n+1)]
        final = set(test) - set(nums)
        print(final)


if __name__ == "__main__":
    s = Solution()
    nums = [1,1]
    s.findDisappearedNumbers(nums)