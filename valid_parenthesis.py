def valid_paranthasis(s):

    para = {")":"(","]":"[","}":"{"}

    stack = []

    for i in s:
        if stack and stack[-1]==para[i]:
            stack.pop()
        else:
            stack.append(i)
    if stack:
        return False
    else:
        return True
    

print(valid_paranthasis("(]"))
        
        
