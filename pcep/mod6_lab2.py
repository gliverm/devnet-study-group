'''
The previous code needs to be improved. It's okay, but it has to be better.

Your task is to make some amendments, which generate the following results:

the output histogram will be sorted based on the characters' frequency (the bigger counter should be presented first)
the histogram should be sent to a file with the same name as the input one, but with the suffix '.hist' (it should be concatenated to the original name)
'''

from os import strerror

srcname = input("File name to inspect?: ")

try:
    chdict = {}
    for line in open(srcname, 'r'):
        for ch in line:
            if ch.isalpha():
                if ch.lower() in chdict:
                    chdict[ch.lower()] += 1
                else:
                    chdict[ch.lower()] = 1
except IOError as e:
    print('I/0 error occurred: ', strerror(e.errno))

try:
    # Don't like the following so much favoring naming of key and val fields
    # for item in sorted(chdict.items(), key=lambda x: x[1], reverse=True):
    #     print(f'{item[0]} -> {item[1]}')
    destname = srcname[0:srcname.rfind('.')] + '_hist.' + srcname[srcname.rfind('.')+1:]
    writefile = open(destname, 'w')
    for key, val in sorted(chdict.items(), key=lambda x: x[1], reverse=True):
        print(f'{key} -> {val}')
        writefile.write(f'{key} -> {val}\n')
except IOError as e:
    print('I/0 error occurred: ', strerror(e.errno))