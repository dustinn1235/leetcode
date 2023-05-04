class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = [(value, timestamp)]
        else:
            self.hashmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.hashmap.get(key, [])
        res = ""

        l = 0
        r = len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if arr[m][1] == timestamp:
                return arr[m][0]
            
            if arr[m][1] < timestamp:
                l = m + 1
                res = arr[m][0]
            else:
                r = m - 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)