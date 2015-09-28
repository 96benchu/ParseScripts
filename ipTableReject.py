import sys
import os.path

#Run script with file "iptables.out" in the directory
#generates a logfile with ip addresses with new activity or increased activity

localA = []
localB = []
log_statement = []

def file_len(fname):
    with open(fname) as f:
        i = -1
        for i, l in enumerate(f):
            pass
    return i + 1

def prevData():
    #prevD is filename of previous data
    if(os.path.isfile('prev.txt')):
        length = file_len('prev.txt')
        existingF = open("prev.txt",'r+')
    else:
        existingF = open('prev.txt','w')
        length = file_len('prev.txt')

    
    
    for i in range(length):
        toParse = existingF.readline()
        pkts = toParse.split()
        localA.append(pkts)
    existingF.close()




def newData():
    #newD is filename of new Data
    length = file_len('iptables2.out')

    newF = open('iptables2.out','r+')
    #2 readlines for first two lines
    newF.readline()
    newF.readline()
    for i in range(length-8):
        toParse = newF.readline()
        pkts = toParse.split()
        localB.append([pkts[0],pkts[7]])
    newF.close()

def convert():
    for i in range(len(localA)):
        pkts = localA[i]
        pkts[0] = int(pkts[0])

    for i in range(len(localB)):
        pkts = localB[i]
        numpkts = pkts[0]
        last = numpkts[-1]
        if last == 'K':
            pkts[0] = int(numpkts[:-1]+'000')
        elif last == 'M': 
            pkts[0] = int(numpkts[:-1]+'000000')
        elif last == 'G': 
            pkts[0] = int(numpkts[:-1]+'000000000')
        else:
            pkts[0] = int(pkts[0])

def compare():
    for i in range(len(localA)):
        old = localA[i]
        new = localB[i]
        if new[0] > old[0]:
            log_statement.append(new[1] + ' has increased in activity')
        else:
            # log_statement.append(new[1] + ' has ceased activity')
            pass
    print
    for i in range(len(localA),len(localB)):
        new = localB[i]
        log_statement.append(new[1] + ' is a new ip address demonstrating activity')

def replace():
    existingF = open('prev.txt','r+')
    existingF.truncate()
    for i in range(len(localB)):
        pkts = localB[i]
        existingF.write(str(pkts[0]) + ' ' + pkts[1] + '\n')
    existingF.close()

def makeLog():
    logfile = open('log.txt','w')
    if len(log_statement) == 0:
        logfile.write('no increase in activity\n')
    for i in range(len(log_statement)):
        logfile.write(log_statement[i] + '\n')
    logfile.close()


prevData()
newData()
convert()
compare()
replace()
makeLog()