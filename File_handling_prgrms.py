  ############# FILE HANDLING #############

""" WRITE A STATEMENT IN PYTHN TO OPEN A TEXT FILE "MARKER.TXT" SO THAT EXISTING CONTENT CAN BE READ FROM IT."""

file = open("MARKER.txt","r")

       '''(OR)'''

file = open("MARKER.txt","r+")




""" WRITE A STATEMENT IN PYTHON TO OPEN A TEXT FILE "DATA.TXT" SO THAT NEW CONTENTS CAN BE WRITTEN IN IT."""

file = open("DATA.txt","w")

        '''(OR)'''

file = open("DATA.txt","w+")




""" WRITE A STATEMENT IN PYTHON TO OPEN A TEXT FILE "STORY.TXT" SO THAT NEW CONTENTS CAN BE ADDED AT THE END OF IT."""

file = open("STORY.txt","a")

        '''(OR)'''

file = open("STORY.txt","a+")




""" WRITE A FUNCTION "ABLINES()" IN PYTHON TO READ CONTENTS FROM A TEXT FILE "LINES.TXT" TO DISPLAY THOSE LINES, WHICH ARE EITHER STARTING WITH AN ALPHABET 'A' OR STARTING WITH ALPHABET 'B'.
FOR EXAMPLE:
     IF THE CONTENT OF THE FILE IS ;
         A boy is playing outside
         The playground is big
         Banyan tree is in the ground

     The function should display;
         A boy is playing outside
         Banyan tree is in the ground
"""


def ABLINES():
    file = open('LINES.txt','r')
    lines = file.readlines()
    for word in lines:
        if word[0] == 'A' or word[0] == 'B':
            print word
    file.close()

ABLINES()





""" WRITE A FUNCTION "SHORTWORDS()" IN PYTHON TO READ CONTENTS FROM A TEXT FILE "WORDBANK.TXT" AND DISPLAY THOSE WORDS, WHICH ARE LESSER THAN 5 CHARACTERS.
FOR EXAMPLE:
     IF THE CONTENT OF THE FILE IS ;
         The vixen was waiting. Dappled sunlight fell around her onto the soft
         dirt beneath the orange trees.

    The function should display;
        The
        was
        fell
        her
        onto
        the
        soft
        dirt
        the
"""

def SHORTWORDS():
    c = 0
    file = open("WORKBANK.txt","r")
    line = file.read()
    word = line.split()
    for words in word:
        if len(words) < 5:
            print words
    file.close()

SHORTWORDS()






""" WRITE A FUNCTION "WORDCOUNT()" IN PYTHON TO READ CONTENTS FROM A TEXT FILE "WRITER.TXT", TO COUNT AND DISPLAY THE OCCURRENCE OF THE WORD "IS" OR "TO" OR "UP".
FOR EXAMPLE:
     IF THE CONTENT OF THE FILE IS ;
         It is up to us to take care of our surrounding. It is not possible only for the government to take responsibility.

     The function should display;
         Count of IS TO and UP is 6
"""

def WORDCOUNT():
    count = 0
    file = open("WRITER.txt","r")
    line = file.read()
    word = line.split()
    for w in word:
        if w == "is" or w == "up" or w == "to":
            count = count + 1
            print ("Count of IS TO and UP is:",count)
    file.close()

WORDCOUNT()







""" WRITE A FUNCTION "AEDISP()" IN PYTHON TO READ LINES FROM A TEXT FILE "WRITER.TXT", AND DISPLAY THOSE LINES, WHICH ARE STARTING EITHER WITH 'A' OR 'E'.
FOR EXAMPLE:
     IF THE CONTENT OF THE FILE IS ;
         A clean environment is necessary for our good health.
         We should take care of our environment.
         Educational institutions should take the lead.

    The function should display;
        A clean environment is necessary for our good health.
        Educational institutions should take the lead.
"""

def AEDISP():
    file = open("WRITER.txt",'r')
    lines = file.readlines()
    for word in lines:
        if word[0] == "A" or word[0] == "E":
            print word
    file.close()

AEDISP()






""" WRITE A FUNCTION "COUNTWORD()" IN PYTHON TO READ LINES FROM A TEXT FILE "CHECK.TXT", AND DISPLAY NO OF WORDS IN THE TEXT FILE."""
#To count and display the no of words in a text file


def COUNTWORD():
    file = open("CHECK.txt",'r')
    count = 0
    fileread = file.read()
    word = fileread.split()
    for x in word:
        count + = 1
        print ("Number of words in the file:",count)
        print x
    file.close()

COUNTWORD()





""" WRITE A FUNCTION "COUNTLINE()" IN PYTHON TO READ LINES FROM A TEXT FILE "CHECK.TXT", AND DISPLAY NO OF LINES IN THE TEXT FILE."""
#To count and display the no of lines in a text file


def COUNTLINE():
    file = open("CHECK.txt",'r')
    count = 0
    fileread = file.readlines()
    for x in fileread:
        file.readline()
        count + = 1
        print ("Number of lines in the file:",count)
        print x
    file.close()

COUNTLINE()
