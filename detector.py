## FLOW:
## IMPORT CLIPBOARD VIA COPY PASTE INTO LIST -> FETCH ALL LINES WITH -BAN OR -MULTIBAN -> FETCH NUMBERS FROM MESSGAGE -> PUT EACH NUMBER INTO A LIST -> MAKE INTO A STRING WITH EACH LIST OBJECT BEING A NEW LINE -> OUTPUT INTO A TXT FILE -> CHECK FOR OTHER TXT'S IN DIRECOTRY 'DUMP' -> COMPILE INTO TXT IN FOLDER 'FINAL OUTPUT'

## DETECTOR.PY ##

# Import Modules #
import string
from string import digits
import re
# Import Modules #

global i

length = 30 #length of menu solid bars#
i = 0 #for while loop in fclipboard()

def compiletxts():
    print("placeholder")

def fclipboard(): ## Asks user to paste clipboard so it can read and fetch ID's
    global i
    print("Paste in, press enter then Cntrl D or Cntrl Z to finish input.")
    contents = []
    while True:
            try:
                line = input()
            except EOFError:
                break
            contents.append(line)
    while i < len(contents):
        current = contents[i]
        current = ' '.join(c for c in current if c in digits)
        current = current.replace(" ", "")
        contents[i] = current
        i += 1
    multiline = contents[0:]
    eachSeperate = "\n".join(multiline)
    print(eachSeperate)
    file = open('./dump/ids.txt', 'w')
    file.write(eachSeperate)
    file.close()


def menu(): # MAKE CHOICES (Compile, Fetch Clipboard)
    ## READ & PRINT MENU FILE ##
    menutxt = open("menu.txt", "r")
    print(menutxt.read())
    ##REQUESTS AND CHECKS USER INPUT (Not case sensetive)
    menuchoice = input("Input your choice \n >> ")
    menuchoice = str(menuchoice.upper())

    if menuchoice == "C":
        compiletxts()
        menu()
    elif menuchoice == "F":
        fclipboard()
        menu()



menu()