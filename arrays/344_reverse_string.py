
from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)-1
        st = n//2
        print(n)
        for i in range(n,st,-1):
            
            s[i],s[n-i] = s[n-i],s[i]
          



if __name__ == "__main__":

    s = ["s","a","i","v","a","m","s","h","i"]

    sol = Solution()
    sol.reverseString(s)
    print(s)



