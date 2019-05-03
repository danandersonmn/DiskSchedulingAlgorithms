#Daniel Anderson
#Spring 2019
#due May 3, 2019
#Operating Systems
#simulator classes for mechanical disk scheduling algorithms
from records import Records

cylinders = 200


# scan algorithm
# The head will move in one direction servicing requests until it reaches the end of the disk, at which point it will reverse direction

##############################################################################################################
class cscanMode:

    def __init__(self, queue, headpos):

        self.headPos = headpos

        if not isinstance(queue, list):
            raise TypeError("queue must be set to an list")
        self.name = "c-scan algorithm"
        print()
        print(self.name)
        self.requestList = queue.copy()

    def run(self):
        print("starting run")
        self.records = Records()
        # print(len(self.requestList))
        # print(self.requestList)
        self.startIndex = 0
        self.requestList.sort()
        finished = False
        endPos = cylinders

        hp = self.headPos
        while len(self.requestList) > 0:
            for track in range(hp, endPos, 1):
                if track in self.requestList:
                    # print(track)
                    self.nextTrack = track
                    self.requestList.remove(track)
                    self.records.addRecord(self.headPos, self.nextTrack)
                    self.headPos = self.nextTrack
                if track == 199:
                    hp = 0

        print(self.records)


#########################################################################################################################
# scan algorithm
# The head will move in one direction servicing requests until it reaches the end of the disk, at which point it will reverse direction


class scanMode:
    def __init__(self, queue, headpos):
        self.headPos = headpos

        if not isinstance(queue, list):
            raise TypeError("queue must be set to an list")
        self.name = "scan algorithm"
        print()
        print(self.name)
        self.requestList = queue.copy()

    def run(self):

        print("starting run")
        self.records = Records()
        # print(len(self.requestList))
        # print(self.requestList)
        self.startIndex = 0
        self.requestList.sort()
        finished = False
        endPos = cylinders
        hp = self.headPos
        direction = 1  # values 1 or -1
        while len(self.requestList) > 0:
            for track in range(hp, endPos, direction):
                if track in self.requestList:
                    # print(track)
                    self.nextTrack = track
                    self.requestList.remove(track)
                    self.records.addRecord(self.headPos, self.nextTrack)
                    self.headPos = self.nextTrack
                if track == 199:
                    direction = -1
                    endPos = -1
                    hp = 199

                if track == 0:
                    endPos = cylinders
                    direction = 1
                    hp = 0
        print(self.records)


###################################################################################################
class SSTF:

    def __init__(self, queue, trackStartPos):

        self.currentTrack = trackStartPos
        if not isinstance(queue, list):
            raise TypeError("queue must be set to an list")
        self.name = "shortest seek time first"
        print()
        print(self.name)
        self.queue = queue.copy()

    def selectClosetTrack(self):
        self.minIndex = 0  # setting to first index and assuming there is atleast one
        self.diff = abs(self.queue[0] - self.currentTrack)  # using first index to start with

        for i in range(len(self.queue)):
            # print("index: " + str(i) + ", diff: " + str(abs(self.currentTrack - self.queue[i])) + ", value: " + str(self.queue[i]))
            if abs(self.currentTrack - self.queue[i]) < self.diff:
                self.diff = abs(self.currentTrack - self.queue[i])
                self.minIndex = i

        # print("removing: " + str(self.minIndex ))
        return self.queue.pop(self.minIndex)

    def run(self):
        print("starting run")
        self.records = Records()

        for i in range(len(self.queue)):
            self.nextTrack = self.selectClosetTrack()
            self.records.addRecord(self.currentTrack, self.nextTrack)

            self.currentTrack = self.nextTrack

        print(self.records)


###################################################################################################
class FIFO:

    def __init__(self, queue, trackStartPos):

        self.currentTrack = trackStartPos
        if not isinstance(queue, list):
            raise TypeError("queue must be set to an list")
        self.name = "first in first out"
        print()
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
        print("length of request list: " + str(len(self.queue)))
        for i in range(len(self.queue)):
            self.nextTrack = self.accessNextTrack()
            self.records.addRecord(self.currentTrack, self.nextTrack)

            self.currentTrack = self.nextTrack

        print(self.records)


###################################################################################################


# similiar to fifo except reversing queue before processing. This works as it is working with full queue at once and not recieving new items
class LIFO:

    def __init__(self, queue, trackStartPos):

        self.currentTrack = trackStartPos
        if not isinstance(queue, list):
            raise TypeError("queue must be set to an list")
        self.name = "last in first out"
        print()
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
        print("length of request list: " + str(len(self.queue)))
        for i in range(len(self.queue)):
            self.nextTrack = self.accessNextTrack()
            self.records.addRecord(self.currentTrack, self.nextTrack)

            self.currentTrack = self.nextTrack

        print(self.records)

###################################################################################################

# scan algorithm
# The head will move in one direction servicing requests until it reaches the end of the disk, at which point it will reverse direction


class nstepscan:
    def __init__(self, queue, headpos, queuesize):
        self.headPos = headpos
        self.queueSize = queuesize
        if not isinstance(queue, list):
            raise TypeError("queue must be set to an list")
        self.name = "n-scan step scan algorithm"
        print()
        print(self.name)
        self.requestList = queue.copy()

    def run(self):

        print("starting run")
        self.records = Records()
        # print(len(self.requestList))
        # print(self.requestList)
        self.startIndex = 0

        hp = self.headPos
        endPos = cylinders
        direction = 1  # values 1 or -1
        while len(self.requestList) > 0:
            self.activeRequestQueue = []
            for i in range(self.queueSize):
                #print(i)
                if len(self.requestList) > 0:
                    self.activeRequestQueue.append(self.requestList.pop(0))
            while len(self.activeRequestQueue) > 0:

                for track in range(hp, endPos, direction):
                    if track in self.activeRequestQueue:
                        #print("while " + str(track))
                        self.nextTrack = track
                        self.activeRequestQueue.remove(track)
                        self.records.addRecord(self.headPos, self.nextTrack)
                        self.headPos = self.nextTrack

                    if track == 199:
                        direction = -1
                        endPos = -1
                        hp =cylinders -1;
                    elif track == 0:
                        endPos = cylinders
                        hp = 0
                        direction = 1
        print(self.records)

#########################################################################################################################

# fscan algorithm
#

#incomplete
class fscan:
    def __init__(self, queue, headpos, queuesize):
        self.headPos = headpos
        self.queueSize = queuesize
        if not isinstance(queue, list):
            raise TypeError("queue must be set to an list")
        self.name = "n-scan step scan algorithm"
        print()
        print(self.name)
        self.requestList = queue.copy()

    def run(self):

        print("starting run")
        self.records = Records()
        # print(len(self.requestList))
        # print(self.requestList)
        self.startIndex = 0


        endPos = cylinders
        direction = 1  # values 1 or -1
        while len(self.requestList) > 0:
            self.activeRequestQueue = []
            for i in range(self.queueSize):
                #print(i)
                if len(self.requestList) > 0:
                    self.activeRequestQueue.append(self.requestList.pop(0))
            while len(self.activeRequestQueue) > 0:
                for track in range(self.headPos, endPos, direction):
                    if track in self.activeRequestQueue:
                        # print(track)
                        self.nextTrack = track
                        self.activeRequestQueue.remove(track)
                        self.records.addRecord(self.headPos, self.nextTrack)
                        self.headPos = self.nextTrack
                    if track == 199:
                        direction *= -1
                        endPos = -1

                    if track == 0:
                        endPos = cylinders
                        direction *= -1
        print(self.records)

#########################################################################################################################




