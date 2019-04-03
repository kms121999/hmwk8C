#
#
#
#

WIDTH = 50
TEXTFILE = 'short_story.txt'


INTRO = "Welcome to the Sentence Formatter"

def intro():
    print(INTRO.center(WIDTH, ' '))


def split():
    indexStart = 0
    indexEnd = WIDTH + 1

    yourString = "your string"*50

    while indexStart < len(yourString):
        split = False
        if indexEnd >= len(yourString):
                split = True
        while not split:
            if yourString[indexEnd] == ' ':
                split = True
            else:
                indexEnd -= 1
                
        print(yourString[indexStart:indexEnd])
        indexStart = indexEnd + 1
        indexEnd += WIDTH
            

