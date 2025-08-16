class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = []
        for i in s:
            if i in "aeiouAEIOU":
                stack.append(i)
        result = []
        for i in s:
            if i not in "aeiouAEIOU":
                result.append(i)
            else:
                result.append(stack.pop())
        return "".join(result)

        
if __name__ == '__main__':
    s = Solution()
    st = "IceCreAm"
    s.reverseVowels(st)
