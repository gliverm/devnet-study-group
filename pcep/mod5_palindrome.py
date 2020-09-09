def ispalidrome(s):
    tst = s.lower().replace(" ", "")
    rslt = True
    #for i in range(len(tst)):
    for i in range(len(tst) // 2 + 1):
        if tst[i] != tst[-1 - i]:
            rslt = False
            break
    return rslt

s = input("Enter string to test for palidrome: ")
print(ispalidrome(s))

# Another solution and far easier
# ... and check if the word is equal to reversed itself
# if len(text) > 1 and text.upper() == text[::-1].upper():
# 	print("It's a palindrome")
# else:
# 	print("It's not a palindrome")