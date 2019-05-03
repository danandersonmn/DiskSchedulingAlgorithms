

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
