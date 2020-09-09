'''
Prof. Jekyll conducts classes with students and regularly makes notes in a text file. Each line of the file contains 3 elements: the student's first name, the student's last name, and the number of point the student received during certain classes.

The elements are separated with white spaces. Each student may appear more than once inside Prof. Jekyll's file.

Your task is to write a program which:

asks the user for Prof. Jekyll's file name;
reads the file contents and counts the sum of the received points for each student;
prints a simple (but sorted) report, just like this one:

'''

from os import strerror

class StudentsDataException(Exception):
	pass

class BadLine(StudentsDataException):
    def __init__(self, line, message="Bad Student File line."):
        self.msg = message
        self.line = line

class FileEmpty(StudentsDataException):
    def __init__(self, filename, message="File is empty."):
        self.msg = message
        self.filename = filename

#srcname = input("File name to inspect?: ")
srcname = "students.txt"
#srcname = "students_empty.txt"

try:
    sdict = {}
    sfile = open(srcname, 'r')
    line = sfile.readline()
    if not line:
        raise FileEmpty(srcname)
    while line:
        linelst = line.split()
        student = " ".join([linelst[0], linelst[1]])
        if student in sdict:
            sdict[student] += float(linelst[2])
        else:
            sdict[student] = float(linelst[2])
        line = sfile.readline()
except FileEmpty as fe:
    print(f'ERROR: {fe.msg}  filename: {fe.filename}')
    raise
except BadLine as bl:
    print(f'ERROR: {bl.msg}  line: {bl.line}')
    raise
except IOError as e:
    print('I/0 error occurred: ', strerror(e.errno))
    raise

print(sdict)
# try:
#     destname = srcname[0:srcname.rfind('.')] + '_new.' + srcname[srcname.rfind('.') + 1:]
#     writefile = open(destname, 'w')
#     for key, val in sorted(sdict.items()):
#         print(f'{key} -> {val}')
#         writefile.write(f'{key} -> {val}\n')
# except IOError as e:
#     print('I/0 error occurred: ', strerror(e.errno))