txt1 = input("Enter first txt: ").replace(" ", "").lower()
txt2 = input("Enter second txt: ").replace(" ", "").lower()

hidden = True
start = 0
for l in txt1:
    start = txt2.find(l, start)
    if start == -1:
        hidden = False
        break

print("Hidden: ", hidden)

# #Another solution
# word = input("Enter the word you wish to find: ").upper()
# strn = input("Enter the string you wish to search through: ").upper()
#
# found = True
# start = 0
#
# for ch in word:
# 	pos = strn.find(ch, start)
# 	if pos < 0:
# 		found = False
# 		break
# 	start = pos + 1
# if found:
# 	print("Yes")
# else:
# 	print("No")