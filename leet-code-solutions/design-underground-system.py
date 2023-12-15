class UndergroundSystem:

    def __init__(self):
        self.checkindict = {}  
        self.coll = {}

    def checkIn(self, id, stationName, t):
        self.checkindict[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        station1, time = self.checkindict[id]
        station2 = stationName
        traveled = t - time

        part = (station1, station2)
        if part not in self.coll:
            self.coll[part] = {'timeTaken': 0, 'count': 0}

        self.coll[part]['timeTaken'] += traveled
        self.coll[part]['count'] += 1

    def getAverageTime(self, startStation, endStation):
        part = (startStation, endStation)
        if part in self.coll:
            timeTaken = self.coll[part]['timeTaken']
            count = self.coll[part]['count']
            return timeTaken / count
        else:
            return 0  
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)