class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        freq = {}
        vowels = set("aeiou")
        max_count = 0
        count=0
        n = len(s)
        start = 0
        for end in range(n):
            if s[end] in vowels:
                count+=1
            if end-start+1>k:
                if s[start] in vowels:
                    count-=1
                start+=1
            
            if end-start+1 == k:
                max_count = max(max_count,count)
        return max_count
if __name__ == "__main__":
    sol = Solution()
    s = "abciiidef"
    k = 3
    print(sol.maxVowels(s,k))