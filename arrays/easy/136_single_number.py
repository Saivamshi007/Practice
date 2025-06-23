from typing import List
class Solution:
    def single_number(self,nums:List[int])->int:
        hash = {}
        for num in nums:
            hash[num] = 1+ hash.get(num,0)
        for key,val in hash.items():
            if val==1:
                return key

    
if __name__ == "__main__":
    sol = Solution()
    nums = [3,3,4,5,5,7,7]
    print(sol.single_number(nums))