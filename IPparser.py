import sys
import os.path
import re

#Run script with file "iptables.out" in the directory
#generates a logfile with ip addresses with new activity or increased activity

localB = []
log_statement = []

def file_len(fname):
    with open(fname) as f:
        i = -1
        for i, l in enumerate(f):
            pass
    return i + 1

def newData():
    #newD is filename of new Data
    # length = file_len('access.out')
    newF = open('access.out', encoding="utf8")
    #2 readlines for first two lines
    for toParse in newF:
        # toParse = newF.readline()
        # print(toParse)
        pkts = re.split("\x05|\x01|\x03",toParse);
        # print(pkts[8])
        localB.append([pkts[5],pkts[7]])
    newF.close()

def analyze():
    for i in range(len(localB)):
        if "www." not in localB[i][0]:
            str1 = localB[i][1]
            log_statement.append(str1[1:])
        else:  
            str1 = localB[i][0]
            log_statement.append(str1[1:])



def makeLog():
    logfile = open('log2.txt','w')
    for i in range(len(log_statement)):
        if (re.search('[a-zA-Z]', log_statement[i]) is not None):
            if log_statement[i] != "GET":
                write = log_statement[i]
                logfile.write(write + '\n')
    logfile.close()

newData()
analyze()
makeLog()

# etx = weird symbol ENQ = | SOH = space

