class UndergroundSystem:
    def __init__(self):
        self.time = {}
        self.check = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.check[id]
        if startStation not in self.time:
            self.time[startStation] = {}
        if stationName not in self.time[startStation]:
            self.time[startStation][stationName] = (t - startTime, 1)
        else:
            time, n = self.time[startStation][stationName]
            self.time[startStation][stationName] = (time + t - startTime, n + 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return (
            self.time[startStation][endStation][0]
            / self.time[startStation][endStation][1]
        )


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
