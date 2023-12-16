class AuthenticationManager:
  def __init__(self, timeToLive: int):
    self.timeToLive = timeToLive
    self.timeExpired = {}
    self.times = collections.defaultdict(int)

  def generate(self, tokenId: str, currentTime: int) -> None:
    self.timeExpired[tokenId] = currentTime
    self.times[currentTime] += 1

  def renew(self, tokenId: str, currentTime: int) -> None:
    expiryTime = self.timeExpired.get(tokenId)
    if expiryTime is None or currentTime >= expiryTime + self.timeToLive:
      return
    del self.times[expiryTime]
    self.timeExpired[tokenId] = currentTime
    self.times[currentTime] += 1

  def countUnexpiredTokens(self, currentTime: int) -> int:
    expiryTimeThreshold = currentTime - self.timeToLive + 1
    for expiryTime in list(self.times.keys()):
      if expiryTime < expiryTimeThreshold:
        del self.times[expiryTime]
    return sum(self.times.values())


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)