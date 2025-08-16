class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i=j=0
        for i in range(len(haystack)-len(needle)+1):
            j = 0
            while j<len(needle) and  haystack[i+j] == needle[j]:
                    j+=1
               
            if j==len(needle):
                return i
            
        return -1
        
        

if __name__ == "__main__":
    sol = Solution()
    hay = "aaa"
    needle = "aaaa"
    print(sol.strStr(hay,needle))
