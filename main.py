# The purpose of this script is to read a file and generate the total number of times a word appears in the file.
# It should accept a file as an input and the output should be a number

import fileinput

def test():
    keyword = "This"
    number = 0
    for line in fileinput.input(files= 'Test.txt'):
        word = line.split(sep=' ')
        for i in word:
            if keyword == i:
                number += 1
    return number

print(test())
