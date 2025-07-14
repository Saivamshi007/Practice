from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_max = 0
        end = len(prices)-1
        for start in range(end):
            sub_max = max(prices[start+1:])
            sub_max = sub_max - prices[start]
            if sub_max > total_max:
                total_max = sub_max
        return total_max



if __name__== "__main__":
    sol = Solution()
    prices = [7,1,5,3,6,4]
    print(sol.maxProfit(prices))
