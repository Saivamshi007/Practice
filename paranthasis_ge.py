def paranthasis_gen(n):
    result = []

    def para(open,close,stack):
        if open == close == n:
            result.append("".join(stack))
            return
        
        if open<n:
            stack.append("(")
            para(open+1,close,stack)
            stack.pop()
        if close<open:
            stack.append(")")
            para(open,close+1,stack)
            stack.pop()

    para(0,0,[])
    return result

print(paranthasis_gen(2))

