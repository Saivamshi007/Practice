from typing import List
def flatten(list,final):
    for i in list:
        if isinstance(i,List):
            flatten(i,final)
        else:
            final.append(i)


lis = [1,2,[1,2],[1,[2,3,[1,4]]]]
final = []
flatten(lis,final)
print(final)