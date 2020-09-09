def readint(prompt, min, max):

    done = False
    while not done:
        try:
            val = int(input(prompt))
            assert val >= min and val <= max
            done = True
        except AssertionError:
            print("Error: the value is not within permitted range (" + str(min) + ".." + str(max)+ ")")
        except:
            print("Error: wrong input")

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)