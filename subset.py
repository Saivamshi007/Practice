def gen_sunsets(input):
    result =[]
    

    def subset(start,path):
        result.append(path.copy())
        for i in range(start,len(input)):
            path.append(input[i])
            subset(i+1,path)
            path.pop()
    subset(0,[])
    return result

print(gen_sunsets([1,2,2]))
