from collections import Counter
from typing import List
class Solution:
    def majority_element(self,nums:List[int])->int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count+=1
            else:
                count-=1
        return candidate
        counter = Counter(nums)
        maj = max(list(counter.values()))


        for key, val in counter.items():
            if val == maj:
                return key


if __name__ == "__main__":
    nums = [3,2,6,3,4]
    sol = Solution()
    print(sol.majority_element(nums))