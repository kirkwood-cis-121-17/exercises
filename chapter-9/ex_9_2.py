# Programming Exercise 9-2
#
# Program for memory drill of state capitals.
# This program picks a random state name from a dictionary to prompt for a capital,
# compares the user input, updates correct or incorrect score, loops until quit,
# then outputs the number right and wrong.



# to generate random questions, import the random module



# define the main function

    # Initialize capitals dictionary with names of states and capitals

                
    # define local int variables for correct, incorrect and index

    # define local boolean variable for another question (true)

    # define local string variables for current state, question and user solution


    # game loop - while another question is true, continue


        # define an iterator for capitals dictionary to allow choosing by number

        # Get a random index value from 0 to capitals length -1

        
        # use a for loop to loop in range index - 1
        # (we need to stop early to allow for one last __next__() call after loop ends) 

            # call the __next__() iterator method to increment the iterator

        # get current current state from the iterator using the __next__() method again

        
        # use the current state to build a question, letting user know '0' quits

        # prompt for the user solution with the question

        # if input was 0, user wants to quit the game.

            # set another question = False to stop the game loop
        
        # else if user solution matches the capitals entry for the current state

            # increment correct score and print success message
            # since it was correct, you may remove current state from dictionary with del

        # else (user did not quit or provide a correct solution)

            # increment incorrect score and print failure message


    # print game over message with number correct and incorrect



# Call the main function to start the program


