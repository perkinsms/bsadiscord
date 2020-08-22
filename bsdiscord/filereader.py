#!/usr/bin/python3

# reads rank advancement data from a text file. A typical file line looks like this:
# s%1%a%Show your scoutmaster  . . . .
# the result of this should be a dict that you can look up like this:
#
#
#  For second class requirement 2b: rankAdvancementData["2"]["2"]["b"]
def readRankData(files):
    data = {}
    for file in files:
        filehdl = open(file, 'r')
        lines = filehdl.readlines()
        filehdl.close()
        for line in lines:
            (rank, requirement, subrequirement, reqtext) = line.split('%')
            if not subrequirement:
                subrequirement = requirement
            if not rank in data.keys():
                data[rank] = {}
            if not requirement in data[rank].keys():
                data[rank][requirement] = {}
            data[rank][requirement][subrequirement] = reqtext
    return data

if __name__ == "__main__":

    RANKFILESDIR = 'rankfiles'

    FILESTOREAD = ['scout.txt', 'tenderfoot.txt', \
               'secondclass.txt', 'firstclass.txt', \
               'star.txt', 'life.txt', 'eagle.txt']

    FILESTOREAD = list(map(lambda file: RANKFILESDIR + "/" + file, FILESTOREAD))

    rankAdvancementData = readRankData(FILESTOREAD)
    print("read files = " + str(FILESTOREAD))
    print("ranks = " + str(rankAdvancementData.keys()))
