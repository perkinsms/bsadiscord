""" Rankrequirement.py
Takes in text files containing rank requirement information
(via the filereader module)
and lets the user access the information
"""

import sys
import filereader


# create a dict that maps s to scout, t to tenderfoot, 2 to second class, etc
RANKNAMES = dict(zip(list("st21rle"),\
        ["Scout", "Tenderfoot", "Second Class", "First Class", "Star", "Life", "Eagle"]))

def rankRequirement(commandstring, rankData):
    """ based on a command string like this: rank 1 1 b
    will output string data to show the corresponding rank requirement
    """
    args = commandstring.split()[1:]
    # for when the user provides a subrequirement e.g., first class 1.a.
    if len(args) > 2:
        (rank, requirement, subrequirement) = (args[0], args[1], args[2])
        try:
            output = RANKNAMES[rank] + " " + requirement + subrequirement + "\n"\
                    + rankData[rank][requirement][subrequirement]
        # there wasn't that key in the data
        except KeyError:
            output = "No such requirement or syntax error!"
    # for when the user requests a whole requirement e.g., tenderfoot 6
    elif len(args) == 2:
        (rank, requirement) = (args[0], args[1])
        output = RANKNAMES[rank] + "\n"
        try:
            for subreq in rankData[rank][requirement]:
                output = output + requirement + "." + subreq + ". " + \
                    str(rankData[rank][requirement][subreq])
        # there wasn't that key in the data
        except KeyError:
            output = "No such requirement or syntax error!"
    # for when the user requests a whole rank e.g., scout
    elif len(args) == 1:
        rank = args[0]
        try:
            output = str(rankData[rank])
            # 800 characters of output is the limit before it becomes flooding
            if len(output) > 800:
                raise OutputLengthError
            return output
        # there wasn't that key in the data
        except KeyError:
            output = "No such requirement or syntax error!"
        except OutputLengthError:
            # tell the user it's too long
            # and give the first 800 characters of the requirements
            output = "output too long!" + "\n"\
                    "Here's the beginning: " + "\n"\
                    + output[:800]
    else:   # the user didn't give any arguments other than "rank"
        output = HELPSTRING
    return output


class OutputLengthError(BaseException):
    """outputLengthError - raised when the program is trying to put too much output"""
    # pass


HELPSTRING = """
==============================================================
Rank Requirement output

To see a rank requirement type:

rank x y z

where x is
s for scout
t for tenderfoot
2 for second class
1 for first class
r for star
l for life
e for eagle

y and z are optional and are the requirement number and subreqirement.

Example, for tenderfoot requriement 1a:

rank t 1 a
Present yourself to your leader prepared for an overnight camping trip. Show the personal and camping gear you will use. Show the right way to pack and carry it.
==============================================================
"""


#   Main loop.
if __name__ == "__main__":
    RANKFILESDIR = 'rankfiles'
    FILESTOREAD = ['scout.txt', 'tenderfoot.txt', \
               'secondclass.txt', 'firstclass.txt', \
               'star.txt', 'life.txt', 'eagle.txt']
    FILESTOREAD = list(map(lambda file: RANKFILESDIR + "/" + file, FILESTOREAD))

    rankRequirements = filereader.readRankData(FILESTOREAD)

    while True:
        CMD = input("Type a command (q to quit, h for help): ")
        if   (CMD in ['q', 'Q']):
            sys.exit()
        elif CMD in ['h', 'H']:
            print(HELPSTRING)
        elif CMD.startswith('rank'):
            print(rankRequirement(CMD, rankRequirements))
        else:
            print("Usage: rank x [y] [z]")
