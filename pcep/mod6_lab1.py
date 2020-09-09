"""
A text file contains some text (nothing unusual) but we need to know how often (or how rare) each letter appears in the text. Such an analysis may be useful in cryptography, so we want to be able to do that in reference to the Latin alphabet.

Your task is to write a program which:

asks the user for the input file's name;
reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
prints a simple histogram in alphabetical order (only non-zero counts should be presented)
Create a test file for the code, and check if your histogram contains valid results.
"""
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
    # Unsorted method of printing results
    # for ch, val in chdict.items():
    #     print(f'{ch} -> {val}')
    # Sort by key
    for key in sorted(chdict.keys()):
        print(f'{key} -> {chdict[key]}')
except IOError as e:
    print('I/0 error occurred: ', strerror(e.errno))



