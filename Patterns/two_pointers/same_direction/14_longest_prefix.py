from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_pre = 0
        first = strs[0]
        for i in range(len(first)):
            j=0
            while j<len(strs)  and i<len(strs[j]) and first[i] == strs[j][i]:
                     j+=1
            if j == len(strs):
                max_pre = max(max_pre,i+1)
            else:
                 break
        return first[:max_pre] if max_pre else ""

if __name__=='__main__':
    s = Solution()
    strs = ["cir","car"]
    print(s.longestCommonPrefix(strs))