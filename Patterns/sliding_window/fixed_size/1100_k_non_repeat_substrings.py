class Solution:
    def SubStrings(self,s,k)->int:
        freq = {}
        start = 0
        n = len(s)
        count=0

        for end in range(n):
            freq[s[end]] = freq.get(s[end],0) +1 

            if end-start+1>k:
                freq[s[start]]-=1
                if freq[s[start]] == 0:
                    del freq[s[start]]
                start+=1
            if end-start+1 == k and len(freq) == k:
                count+=1
        return count

if __name__ == "__main__":
    sol = Solution()
    s = "hhavefunonleetcode"
    k = 5
    print(sol.SubStrings(s,k))