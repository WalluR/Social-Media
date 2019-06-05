import re

convIndex = []

def SeperateData (path):
    # splitting text and time to blocks
    with open(path + 'PersonA.txt', 'r') as file:
        personA = file.read()
    with open(path + 'PersonB.txt', 'r') as file:
        personB = file.read()
    with open(path + 'Time.txt', 'r') as file:
        time = file.read()

    # find all the /s int the text
    A = [m.start() for m in re.finditer('/¦s', personA)]
    A1 = [m.start() for m in re.finditer('/¦¦s', personA)]
    B = [m.start() for m in re.finditer('/¦s', personB)]
    B1 = [m.start() for m in re.finditer('/¦¦s', personB)]

    # list that has all the index
    listS = A + A1 + B + B1

    # Now lets to the same with /D
    A = [m.start() for m in re.finditer('/¦d', personA)]
    A1 = [m.start() for m in re.finditer('/¦¦d', personA)]
    B = [m.start() for m in re.finditer('/¦d', personB)]
    B1 = [m.start() for m in re.finditer('/¦¦d', personB)]
    # all /d indexes
    listD = A + A1 + B + B1

    # Our final list with all index
    final = listS + listD
    # transform string to int
    final = [int(x) for x in final]
    # Now our array is order
    final.sort()
    # Celaning the timedata to more readeble form
    cleanedTime = time.strip()
    cleanedTime = cleanedTime.replace('¦', ',')
    # calling the function
    finalTime = splitTime(final, cleanedTime)
    return finalTime, final



#this function will split time in to pieces length of each conversation
#function will return finalTime which is array of = [[],[]] so conversation number 1 is finalTIme[0]
def splitTime(list,time):
    k = 0
    finalTime = []
    for i in list:
        piece = time[k:i]
        k = i
        help = []
        piece = piece.split(",")
        for a in piece:
            if a == '':
                continue
            index = int(a)
            help.append(index)
        finalTime.append(help)
        help = []

    return finalTime

# getting all the data
data1 = SeperateData('data/data1/')
data2 = SeperateData('data/data2/')
data3 = SeperateData('data/data3/')
data4 = SeperateData('data/data3/')
#so data[0] is the times and data[1] is the index

##################################This is where anylyzising happens






