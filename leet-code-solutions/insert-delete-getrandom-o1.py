class RandomizedSet:
  def __init__(self):
    self.vals = []
    self.IndexVal = collections.defaultdict(int)  

  def insert(self, val: int) -> bool:
    if val in self.IndexVal:
      return False
    self.IndexVal[val] = len(self.vals)
    self.vals.append(val)
    return True

  def remove(self, val: int) -> bool:
    if val not in self.IndexVal:
      return False
    index = self.IndexVal[val]
    self.IndexVal[self.vals[-1]] = index
    del self.IndexVal[val]
    self.vals[index] = self.vals[-1]
    self.vals.pop()
    return True

  def getRandom(self) -> int:
    index = random.randint(0, len(self.vals) - 1)
    return self.vals[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()