#Daniel Anderson
#OS Spring 2019
#due may 3, 2019
import random
from records import Records
trackMin = 0
trackMax = 199
cylinders = 200
headPos = 100
queueSize = 1000
requestList = []

requestsFromBook = [55, 58, 39, 18, 90, 160, 150, 38, 184] # table 11.2

print(requestsFromBook)
for x in range(queueSize):
    requestList.append(random.randint(trackMin, trackMax))



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






writeQueueToFile("testqueue.txt", requestList)

fifo(str(requestList))

#scan algorithm
# The head will move in one direction servicing requests until it reaches the end of the disk, at which point it will reverse direction


class cscanMode:
    def __init__(self, queue, headpos):
        self.headPos = headpos

        if not isinstance(queue, list):
            raise TypeError("queue must be set to an list")
        self.name = "c-scan algorithm"
        print(self.name)
        self.requestList = queue.copy()

        self.direction = 1 #direction modifier


    def run(self):
        print("starting run")
        self.records = Records()
        print(len(self.requestList))
        print(self.requestList)
        self.startIndex = 0
        self.requestList.sort()
        finished = False
        endPos = cylinders
        direction = 1 # values 1 or -1
        hp = self.headPos
        while len(self.requestList) > 0:
            for track in range(hp, endPos, direction):
                if track in self.requestList:
                    print(track)
                    self.nextTrack = track
                    self.requestList.remove(track)
                    self.records.addRecord(self.headPos, self.nextTrack)
                    self.headPos = self.nextTrack
                if track == 199:
                    hp = 0



        print(self.records)

cscan = cscanMode(requestsFromBook, headPos)
cscan.run()




#scan algorithm
# The head will move in one direction servicing requests until it reaches the end of the disk, at which point it will reverse direction


class scanMode:
    def __init__(self, queue, headpos):
        self.headPos = headpos

        if not isinstance(queue, list):
            raise TypeError("queue must be set to an list")
        self.name = "scan algorithm"
        print(self.name)
        self.requestList = queue.copy()

        self.direction = 1 #direction modifier


    def run(self):
        print("starting run")
        self.records = Records()
        print(len(self.requestList))
        print(self.requestList)
        self.startIndex = 0
        self.requestList.sort()
        finished = False
        endPos = cylinders
        direction = 1 # values 1 or -1
        while len(self.requestList) > 0:
            for track in range(self.headPos, endPos, direction):
                if track in self.requestList:
                    print(track)
                    self.nextTrack = track
                    self.requestList.remove(track)
                    self.records.addRecord(self.headPos, self.nextTrack)
                    self.headPos = self.nextTrack
                if track == 199:
                    direction *= -1
                    endPos = -1

                if track == 0:
                    endPos = cylinders
                    direction *= -1
        print(self.records)










        #for i in range(len(self.queue)):

           # self.nextTrack = self.selectNextItemInDirection()
            #self.records.addRecord(self.head, self.nextTrack)

           # self.head = self.nextTrack




scan = scanMode(requestsFromBook, headPos)
scan.run()


class SSTF:





    def __init__(self, queue, trackStartPos):

        self.currentTrack = trackStartPos
        if not isinstance(queue, list):
            raise TypeError("queue must be set to an list")
        self.name = "shortest seek time first"
        print(self.name)
        self.queue = queue.copy()








    def selectClosetTrack(self):
        self.minIndex = 0 #setting to first index and assuming there is atleast one
        self.diff = abs(self.queue[0] - self.currentTrack) #using first index to start with

        for i in range(len(self.queue)):
            print("index: " + str(i) + ", diff: " + str(abs(self.currentTrack - self.queue[i])) + ", value: " + str(self.queue[i]))
            if abs(self.currentTrack - self.queue[i]) < self.diff:
                self.diff = abs(self.currentTrack - self.queue[i])
                self.minIndex = i


        print("removing: " + str(self.minIndex ))
        return self.queue.pop(self.minIndex )



    def run(self):
        print("starting run")
        self.records = Records()

        for i in range(len(self.queue)):

            self.nextTrack = self.selectClosetTrack()
            self.records.addRecord(self.currentTrack, self.nextTrack)

            self.currentTrack = self.nextTrack



        print(self.records)




class FIFO:





    def __init__(self, queue, trackStartPos):

        self.currentTrack = trackStartPos
        if not isinstance(queue, list):
            raise TypeError("queue must be set to an list")
        self.name = "first in first out"
        print(self.name)
        self.queue = queue.copy()
        self.pos = 0


    def getQueue(self):

        return self.queue

    def accessNextTrack(self):
        self.pos += 1
        return self.queue.pop(0)

    def run(self):
        print("starting run")
        self.records = Records()
        print(len(self.queue))
        for i in range(len(self.queue)):
            self.nextTrack = self.accessNextTrack()
            self.records.addRecord(self.currentTrack, self.nextTrack)

            self.currentTrack = self.nextTrack



        print(self.records)

#similiar to fifo except reversing queue before processing. This works as it is working with full queue at once and not recieving new items
class LIFO:

    def __init__(self, queue, trackStartPos):

        self.currentTrack = trackStartPos
        if not isinstance(queue, list):
            raise TypeError("queue must be set to an list")
        self.name = "last in first out"
        print(self.name)
        self.queue = queue.copy()

        self.pos = 0

    def copyList(self, in_List):
        self.out_list = []
        for i in in_List:
            self.out_list.append(i)
        return self.out_list

    def getQueue(self):

        return self.queue

    def accessNextTrack(self):
        self.pos += 1
        return self.queue.pop(0)

    def run(self):
        self.queue.reverse()
        print("starting run")
        self.records = Records()
        print(len(self.queue))
        for i in range(len(self.queue)):
            self.nextTrack = self.accessNextTrack()
            self.records.addRecord(self.currentTrack, self.nextTrack)

            self.currentTrack = self.nextTrack



        print(self.records)
# sstf = SSTF(tracklistfrombook, trackStartPos)
# sstf.run()
#
# lifo = LIFO(tracklistfrombook, trackStartPos)
# #print(test.getQueue())
# lifo.run()
#
# fifo = FIFO(tracklistfrombook, trackStartPos)
# #print(test.getQueue())
#
# fifo.run()
#






