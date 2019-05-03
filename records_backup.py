class Records:

    def __init__(self):
        self.records = []
        self.iteraton = 0
        self.totalTrackSeek = 0;

    def addRecord(self, currentTrack, nextTrack):
        self.iteraton += 1
        newRecord = _Record(self.iteraton, currentTrack, nextTrack)
        self.records.append(newRecord)
        self.totalTrackSeek += newRecord.getTrackSeekDistance()
        #print(newRecord)
        #print(str(self.totalTrackSeek))

    def computeAvg(self):

        if self.iteraton > 0:
            return self.totalTrackSeek / self.iteraton

        return 0

    def __repr__(self):
        return "Records"

    def __str__(self):

        for record in self.records:
            print(record)
        return "totalSeekDistance: " + str(self.totalTrackSeek) + ", total num of records: " + str(self.iteraton) + ", avg: " + str(self.computeAvg())

    def printResults(self):
        for record in self.records:
            record.print

class _Record:

    def __init__(self, iteraton, currentTrack, nextTrack):
        self.iteraton = iteraton
        self.currentTrack = currentTrack
        self.nextTrack = nextTrack
        self.numTracksToMove = abs(currentTrack - nextTrack)

    def getTrackSeekDistance(self):
        return self.numTracksToMove

    def __repr__(self):
        return "Record"

    def __str__(self):

        return str("iteraton: " + str(self.iteraton) + ", current track: " + str(self.currentTrack) + ", nextTrack: " + str(self.nextTrack) + ", num of tracks to move: " + str(self.numTracksToMove))
