class Solution:
    def removebackspace(self,s):
        stack =[]
        for i in s:
            if i!='#':
                stack.append(i)
            else:
                stack.pop()
            
        return ''.join(stack)

    def backspaceCompare(self, s: str, t: str) -> bool:

        final_s = self.removebackspace(list(s))
        final_t = self.removebackspace(list(t))
        if final_s != final_t:
            return False
        return True

if __name__ == '__main__':
    sol = Solution()

    s = "ab#c"
    t = "ad#c"

    print(sol.backspaceCompare(s,t))
