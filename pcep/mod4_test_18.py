dct = { 'one':'two', 'three':'one', 'two':'three'}

v = dct['one']
for k in range(len(dct)):
    v = dct[v]

print(v)

# Output is two