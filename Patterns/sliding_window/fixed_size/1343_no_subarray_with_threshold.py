from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        start = 0
        n = len(arr)
        tem_sum = 0
        output = 0

        for end in range(n):
            tem_sum += arr[end]

            if end - start+1>k:
                tem_sum-=arr[start]
                start+=1
            if end-start+1 == k:
                if tem_sum/k >= threshold:
                    output+=1
        return output

    
if __name__ == "__main__":
    sol = Solution()
    arr = [2,2,2,2,5,5,5,8]
    k = 3 
    threshold = 4
    sol.numOfSubarrays(arr,k,threshold)