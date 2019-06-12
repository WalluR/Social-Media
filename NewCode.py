import JohansCode

def splitString(path,split):
    file = open(path, 'r')
    for line in file.readlines():
        fname = line.rstrip().split('¦')  # using rstrip to remove the \n
        i = 0
        index = []
        while i < len(fname):
            if fname[i] == '/' and fname[i + 1] == split:  # rememnber to chech that not going to overbounds!!!!!!
                index.append(i)
            if fname[i] == '/' and fname[i + 2] == split:  ## data is bad so we have to do this
                index.append(i)
            i += 1

        return(index,fname)

# return the splitted time
def splitTime(list,time):
    k = 0
    finalTime = []
    for i in list:
        piece = time[k:i]
        k = i
        finalTime.append(piece)

    return finalTime

# takes text, index returns splitted text
def splitText(text,index):
    array = []
    old = 0
    for i in index:  # split using index
        slice = text[old:i]
        array.append(slice)
        old = i
    return (array)

#takes data and returns the index where to split
def splitInterface(data,split):
    calc = 0
    i = 0
    while i < len(data):
        calc += len(data[i])
        if calc >= split:
            return(i)
        i += 1

def main():
    A = splitString('data/data1/PersonA.txt','s')
    A1 = splitString('data/data1/PersonA.txt', 'd')
    B = splitString('data/data1/PersonB.txt','s')
    B1 = splitString('data/data1/PersonB.txt', 'd')
    final = A[0] + B[0] + A1[0] + B1[0]
    final = [int(x) for x in final]
    # Now our array is order
    final.sort()
    file = open('data/data1/Time.txt', 'r')
    for line in file.readlines():
        time = line.rstrip().split('¦')  # using rstrip to r
    ### doing something ############################
    time = splitTime(final,time) #this retusn time in conversation
    splittedA = splitText(A[1],final) # returns splittes conversation
    splittedB = splitText(B[1], final)  # returns splittes conversation
    split_index = JohansCode.splitter_function('data/data1/')
    index = splitInterface(splittedA,split_index)  # return index where iterface is changing
    return(time[0:index],time[index:len(time)], splittedA[0:index],splittedA[index:len(splittedA)],splittedB[0:index],splittedB[index:len(splittedA)])



