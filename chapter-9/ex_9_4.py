# Programming Exercise 9-4
#
# Program to list the unique words in a text file.
# This program takes the name of a text file from the user,
# reads the file content, splits it into words, then takes a set of unique entries,
# and outputs each entry in the set to the screen.



# define the main function

    
    # define local string variables for file name and file content
    
    # declare empty lists for raw words and word list

    # optionally, declare an empty set for unique words (uniqueWords = set())

    
    # Get file name from user

    # enclose file operations in a try block
        
        # Open the input file for reading
 
        # read the text into file content

        # split the file content into raw words list

        # create a set of unique words from word list

        # Print a message with the number of results.
        
        # convert uniquewords with list() function and assign to word list

        # sort word list with .sort() method


        # loop through the word list

            # print each word to the screen


        # Close the file.


    # use an except block to catch any IOError

        # output a file error message

    # use a generic except block to catch other errors

        # output a generic error message



# Call the main function to start the program


