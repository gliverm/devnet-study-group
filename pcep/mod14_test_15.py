dct = {}
lst = ['a', 'b', 'c', 'd']

for i in range(len(lst) - 1):
    dct[lst[i]] = ( lst[i], )

for i in sorted(dct.keys()):
    k = dct[i]
    print(k[0])

# output; a b c