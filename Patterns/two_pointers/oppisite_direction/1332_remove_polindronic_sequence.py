class Solution:
    def removePalindromeSub(self, s: str) -> int:
        n = len(s)
        res = []
        left,right = 0, n-1
        
        
    def polindrome_checker(self,pol:str):
        left, right = 0, len(pol)-1
        while left<right:
            if pol[left]!=pol[right]:
                return False
            left+=1
            right-=1
        return True

if __name__ == "__main__":
    sol = Solution()
    pol = "aa"
    sol.removePalindromeSub(pol)

