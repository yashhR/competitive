class LRUCache:
    def __init__(self, capacity: int):
        self.pasha = []
        self.k = capacity

    def get(self, key: int) -> int:
        found = False
        for bitch in range(len(self.pasha)-1, -1, -1):
            if self.pasha[bitch][0] == key:
                found = True
                yo = self.pasha.pop(bitch)
                break
        if not found:
            return -1
        self.pasha.append(yo)
        return self.pasha[-1][1]

    def put(self, key: int, value: int) -> None:
        found = False
        for hehe in range(len(self.pasha)):
            if self.pasha[hehe][0] == key:
                found = True
                self.pasha.pop(hehe)
                break
        if not found:
            if len(self.pasha) == self.k:
                self.pasha.pop(0)
        self.pasha.append((key, value))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)