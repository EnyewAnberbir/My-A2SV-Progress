class BrowserHistory:
  def __init__(self, homepage: str):
    self.urls = []
    self.current = -1
    self.last = -1
    self.visit(homepage)

  def visit(self, url: str) -> None:
    self.current += 1
    if self.current < len(self.urls):
      self.urls[self.current] = url
    else:
      self.urls.append(url)
    self.last = self.current

  def back(self, steps: int) -> str:
    self.current = max(0, self.current - steps)
    return self.urls[self.current]

  def forward(self, steps: int) -> str:
    self.current = min(self.last, self.current + steps)
    return self.urls[self.current]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)