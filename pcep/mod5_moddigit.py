bday = input("Enter your birthday [YYYYMMDD or YYYYDDMM or MMDDYYYY]:")

if len(bday) != 8 or not date.isdigit():
    print("Birthday dat must be 8 digits in length")
else:
    while len(bday) != 1:
        lst = list(bday)
        sum = 0
        for num in lst:
            sum += int(num)
        bday = str(sum)

print(bday)

# Better solution follows
# date = input("Enter your birthday date (in the following format: YYYYMMDD or YYYYDDMM, 8 digits): ")
# if len(date) != 8 or not date.isdigit():
# 	print("Invalid date - sorry, we can do nothing with it.")
# else:
# 	# while there is more than one digit in the date...
# 	while len(date) > 1:
# 		sum = 0
# 		# ... sum all the digits...
# 		for dig in date:
# 			sum += int(dig)
# 		print(date)
# 		# ... and store sum inside the string
# 		date = str(sum)
# 	print("Your Digit of Life is: " + date)
