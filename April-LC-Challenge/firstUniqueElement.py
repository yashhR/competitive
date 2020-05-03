"""class FirstUnique:
    uniques = []
    seen = set()
    nums = []
    def __init__(self, nums):
        self.nums = nums
        for i in range(len(nums)):
            if nums[i] not in self.seen:
                self.uniques.append(nums[i])
            else:
                if nums[i] in self.uniques:
                    self.uniques.remove(nums[i])
            self.seen.add(nums[i])

    def showFirstUnique(self) -> int:
        if len(self.uniques):
            return self.uniques[0]
        return -1

    def add(self, value: int) -> None:
        if value in self.uniques:
            self.uniques.remove(value)
        else:
            self.uniques.append(value)
        self.nums.append(value)"""

class FirstUnique:
    def __init__(self, nums):
        self.q = []
        self.dict = {}
        for i in nums:
            self.add(i)

    def showFirstUnique(self) -> int:
        while len(self.q) > 0 and self.dict[self.q[0]] > 1:
            self.q.pop(0)
        if len(self.q) == 0:
            return -1
        else:
            return self.q[0]

    def add(self, value: int) -> None:
        if value in self.dict:
            self.dict[value] += 1
        else:
            self.dict[value] = 1
            self.q.append(value)
# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)

hehe = FirstUnique([7, 7, 7, 7, 7, 7])
print(hehe.showFirstUnique())
hehe.add(7)
hehe.add(3)
hehe.add(3)
hehe.add(7)
hehe.add(17)
print(hehe.showFirstUnique())