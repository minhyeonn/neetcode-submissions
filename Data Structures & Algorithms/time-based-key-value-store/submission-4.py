class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        l = 0
        r = len(self.timeMap[key])-1
        res = ""
        while l<=r:
            m = (l+r)//2
            if self.timeMap[key][m][1]==timestamp:
                return self.timeMap[key][m][0]
            elif self.timeMap[key][m][1]<timestamp:
                res = self.timeMap[key][m][0]
                l = m+1
            else:
                r = m-1

        
        return res