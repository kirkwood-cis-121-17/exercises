# Function to encypher text with a simple, Victorian-style substitution cypher.
# This function accepts a string of plain text as a parameter,
# processes it against a symetric substitution cypher
# and returns the cypher text result.

    # Encryption and decryption are inverse of one another (if a = 0, 0 = a)
    # Define a set of symetric substitution values
    CODE = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',\
            'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',\
            'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2',\
            'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y',\
            'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v',\
            'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s',\
            'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p',\
            'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m',\
            'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j',\
            '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g',\
            '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d',\
            '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a',\
            ':':',',',':':','?':'.','.':'?','<':'>','>':'<',\
            "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=',\
            '{':'[','[':'{','}':']',']':'}'}
        

    # define a local variable to hold the cypher text

    
    # loop through each character in plain text
    for ch in text:
        # If character is space,

            #  it is added to cypher text without conversion

        # otherwise
            # it is used as a key in CODE to find the value to add to cypher text

    # return cypher text


# Function to decypher text using the encypher function, above.
# This function takes a string of cypher text as an argument,
# passes it to the encypher function,
# then returns the result as plain text.

    # define a string variable for plain text

    # pass cypher text to the encypher function and store the result to plain text

    # return plain text

