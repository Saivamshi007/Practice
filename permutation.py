def permutation(input):
    result = []

    def gen_per(path):
        if len(path) == len(input):
            path1 = path.copy()
            result.append(path1)
            return
        for i in input:
            if i not in path:
                path.append(i)
                gen_per(path)
                path.pop()

        
    gen_per([])
    return result
    
print(permutation([1,2,3]))