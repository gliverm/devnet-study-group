# cannot have multiple statements on same line
# print("Greg") print("Python")

d1 = {'Adam Smith':'A', 'Judy Paxton':'B+'}
d2 = {'Mary Louis':'A', 'Patrick White':'C'}
d3 = {}

for item in (d1, d2):
    print(item)
    d3.update(item)

print(d3)