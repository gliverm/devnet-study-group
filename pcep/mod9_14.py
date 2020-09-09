t = [[3-i for i in range (3)] for j in range (3)]
print(t)
s = 0
for i in range(3):
    s += t[i][i]
print(s)

#output is : 3 + 2 + 1 = 6
