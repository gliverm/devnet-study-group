# Caesar cipher
text = input("Enter your message: ")

try:
    shift = int(input("Enter shift value[1..25]:"))
    assert shift >= 1 and shift <= 25
except ValueError:
    print("Error: Shift must be an integer.")
except AssertionError:
    print("Error: Shift must be within the range 1..25.")

cipher = ''
for char in text:
    if char.isalpha():
        code = ord(char) + shift
        if char.isupper():
            if code > ord('Z'):
                code = code - ord("Z") + ord("A") - 1
        else:
            if code > ord('z'):
                code = code - ord("z") + ord("a") - 1
        cipher += chr(code)
    else:
        cipher += char

print(cipher)

# Another method of cipher shift
#
# for char in text:
#     # is it a letter?
#     if char.isalpha():
#         # shift its code
#         code = ord(char) + shift
#         # find the code of the first letter (upper- or lower-case)
#         if char.isupper():
#             first = ord('A')
#         else:
#             first = ord('a')
#         # make correction
#         code -= first
#         code %= 26
#         # append encoded character to message
#         cipher += chr(first + code)
#     else:
#         # append original character to message
#         cipher += char