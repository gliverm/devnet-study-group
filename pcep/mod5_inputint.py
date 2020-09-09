def readint(prompt, min, max):
    done = False
    while not done:
        try:
            num = int(input(prompt))
            assert num >= -10 and num <= 10
            done = True
        except AssertionError:
            print(f"Error: the value is not within permitted range ({min}..{max})")
        except ValueError:
            print("Error: wrong input")
    return num

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)