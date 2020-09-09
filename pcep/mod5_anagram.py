txt1 = input("Enter first txt: ").replace(" ", "").lower()
txt2 = input("Enter second txt: ").replace(" ", "").lower()

rslt = True
if txt1 == "" or txt2 == "":
    rslt = False
elif len(txt1) != len(txt2):
    rslt = False
else:
    for l in txt1:
        if txt2.count(l) > 1:
            rslt = False
            break
print(rslt)

# Another solution I think is better
# str1 = input("Enter the first string: ")
# str2 = input("Enter the second string: ")
#
# # this is what we're going to do with both strings:
# # - remove spaces
# # - change all letters to upper case
# # - convert into list
# # - sort the list
# # - join list's elements into string
# # and finally, compare both strings
# # Let's do it!
#
# strx1 = ''.join(sorted(list(str1.upper().replace(' ',''))))
# strx2 = ''.join(sorted(list(str2.upper().replace(' ',''))))
# if len(strx1) > 0 and strx1 == strx2:
# 	print("Anagrams")
# else:
# 	print("Not anagrams")

