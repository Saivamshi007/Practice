def generate(n):
    result = []

    def backtrack(path):
        if len(path) == n:
            result.append("".join(path)) 
            return
        for i in ["0","1"]:
            path.append(i)
            backtrack(path)
            path.pop()

    
    backtrack([])
    return result


print(generate(3))