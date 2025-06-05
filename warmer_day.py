def warmer_day(temperatures):
    stack = []
    result = [0]*len(temperatures)
    for i,temp in enumerate(temperatures):
        while stack and stack[-1][1]<temperatures[i]:
            idx,temper = stack.pop()
            result[idx]=i-idx
        stack.append((i,temp))
    return result
print(warmer_day([30, 40, 50, 60]))
