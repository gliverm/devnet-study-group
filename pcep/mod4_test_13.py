def f(x):
    if x == 0:
        return 0
    return x + f(x - 1)

print(f(3))

# Output is 6