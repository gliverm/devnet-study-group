lst = [1, 2, 3]
for v in range(len(lst)):
    lst.insert(1, lst[v])
print(lst)

#Output: [1, 1, 1, 1, 2, 3]
