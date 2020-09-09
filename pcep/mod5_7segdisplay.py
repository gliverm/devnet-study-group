# ### ### # # ### ### ### ### ### ###
#   #   # # # #   #     # # # # # # #
# ### ### ### ### ###   # ### ### # #
# #     #   #   # # #   # # #   # # #
# ### ###   # ### ###   # ### ### ###

digits = [
    ["###", "# #", "# #", "# #", "###"],
    ["  #", "  #", "  #", "  #", "  #",],
    ["###", "  #", "###", "#  ", "###"]
]

done = False
while not done:
    try:
        num = input("Enter a non-negative integer: ")
        assert int(num) >= 0
        done = True
    except AssertionError:
        print("Integer must be a positive value.  Try again!!!")
    except ValueError:
        print("Not an integer.  Tray again!!!")

for line in range(5):
    for val in num:
        print(" " + digits[int(val)][line], end="")
    print()

