import fileinput

punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~\n'''

def test(keyword):
    #Initialise count variable
    count = 0

    #Check text for any characters we want to avoid.
    for line in fileinput.input(files= 'Test.txt'):
        for character in line:
            if character in punctuation:
                line = line.replace(character, "")
        
        #Compare each word in text file to our keyword
        word = line.split(sep=' ')
        for i in word:
            if keyword.lower() == i.lower():
                count += 1
    return count