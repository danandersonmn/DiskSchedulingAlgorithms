#Daniel Anderson
#Spring 2019
#due May 3, 2019
#Operating Systems
#simulator classes for mechanical disk scheduling algorithms

import random
from records import Records
from diskAlgorithms import *


trackMin = 0
trackMax = 199
cylinders = 200
headPos = 100
queueSize = 1000
requestList = []

#fifo with book table avg is   55.3
#sstf with book table avg is   27.5
#scan with book table avg is   27.8
#c-scan with book table avg is 35.8





def generateNormalDistribution(num):
    m = 10
    s = 25
    #num = 1000
    output = []
    total = 0
    for i in range(num):
        value = int(random.normalvariate(m, s))
        while value < 0 or value > 199:
            if value > 199:
                value = value % 200
            if value < 0:
                value = value + 200
        output.append(int(value))
        total += value

    count = []
    for i in range(200):
        count.append(0)
        if i in output:
            count[i] = output.count(i)

    print("output")
    print(output)
    print("count")
    print(count)
    print(total)
    print(total/num)
    return output




def writeQueueToFile(path, queue):
    file = open(path, "w+")
    #file.writelines(str(queue))
    for request in queue:
        file.write(str(request))
        file.write("\n")


def genRequests():
    print("gen Requests")


def fifo(queue):
    policyName = "fifo"
    output = []
    file = open(policyName + ".txt", "w+")
    for request in queue:
        file.write(request)


    return output

requestTableToUse = 1
#book table list
if requestTableToUse == 1:
    requestList = [55, 58, 39, 18, 90, 160, 150, 38, 184] # table 11.2
#normal distribution list
if requestTableToUse == 2:
    requestList = generateNormalDistribution(queueSize)
#simple random list
if requestTableToUse == 3:
    for x in range(queueSize):
        requestList.append(random.randint(trackMin, trackMax))
#edge cases
if requestTableToUse == 4:
    requestList = [0, 199, 0, 199, 0, 1]

writeQueueToFile("testqueue.txt", requestList)

for i in requestList:
    if i > 199:
        print(" value out of range: " + str(i))
    if i < 0:
        print(" value out of range: " + str(i))
    if i == 199:
        print(" value equals199 : " + str(i))
    if i == 0:
        print(" value equals0 : " + str(i))


fifo(str(requestList))


nstepscan = nstepscan(requestList, headPos, 5)
nstepscan.run()



cscan = cscanMode(requestList, headPos)
cscan.run()

scan = scanMode(requestList, headPos)
scan.run()

sstf = SSTF(requestList, headPos)
sstf.run()

lifo = LIFO(requestList, headPos)

lifo.run()

fifo = FIFO(requestList, headPos)


fifo.run()







