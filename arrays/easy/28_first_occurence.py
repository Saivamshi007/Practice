class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle in haystack:
            return -1
        word_len = len(needle)
        hay_len = len(haystack)
        start = 0
        end = word_len
        while end<hay_len:
            word = haystack[start:end]
            if haystack[start:end]==needle:
                return start
            start+=1
            end+=1

if __name__ == "__main__":
    sol = Solution()
    hay = "hello"
    needle = "ll"
    sol.strStr(hay,needle)
