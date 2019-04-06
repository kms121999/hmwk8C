#Assignment:    Assignment 8C
#
#Program Name:  ks_assignment_8C.py
#
#Purpose:       To display a file, while keeping line widths within the defined
#               limit.
#
#Author:        Keaton Smith
#Course:        192CIS115.600
#
#Created:       April 5, 2019

# Set named constants
WIDTH = 50  # Width that displayed lines are limited to. # characters
TEXTFILE = 'short_story.txt' # Path to the file to be displayed
HEADER = "Welcome to the Sentence Formatter"

def main(filePath=TEXTFILE, lineWidth = WIDTH):
    #
    #   Function:   main
    #
    #   Author:     Keaton Smith
    #   Date:       April 5, 2019
    #   Filename:   ks_assignment_8C.py
    #
    #   Description:
    #
    #   This function will open a file and display its contents with a max
    #   line width as defined by lineWidth.
    #
    #   Arguments:
    #       str: filePath - The path of the file to be read. Default is TEXTFILE
    #       int: lineWidth - The max line width. Default is WIDTH
    #
    #   Returns:
    #       None
    #

    # Display the programm header
    print(HEADER.center(lineWidth, ' '))
    print()

    # Open the file at filePath
    with open(filePath, 'r') as file:
        # Go through each line of file.
        for line in file:

            # Use variables to keep track of index positions.
            indexStart = 0
            indexEnd = lineWidth
            # Find the length of the line.
            lineLength = len(line)

            # While you are still whithin the length of the line.
            while indexStart < lineLength:
                # Flag identifying when to split the string.
                lineSplit = False

                # If at end of string, print the rest.
                if indexEnd >= lineLength:
                    lineSplit = True
                    print(line[indexStart:indexEnd].rstrip())
                    break

                # While not ready to split...
                while not lineSplit:
                    # Loop until a space is found.
                    if line[indexEnd] == ' ':
                        # If index is at a space character
                        lineSplit = True
                    else:
                        # Else shorten index
                        indexEnd -= 1
                        
                # Display the string chunk
                print(line[indexStart:indexEnd])
                
                # Adjust index variables for the next chunk
                indexStart = indexEnd + 1
                indexEnd += lineWidth

# Call main
main()
