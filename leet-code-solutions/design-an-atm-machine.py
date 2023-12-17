class ATM:
  def __init__(self):
    self.bankNote = [20, 50, 100, 200, 500]
    self.bank = [0] * 5

  def deposit(self, bankNoteCount: List[int]) -> None:
    for i in range(5):
      self.bank[i] += bankNoteCount[i]

  def withdraw(self, amount: int) -> List[int]:
    withdraw = [0] * 5

    for i in reversed(range(5)):
      withdraw[i] = min(self.bank[i], amount // self.bankNote[i])
      amount -= withdraw[i] * self.bankNote[i]

    if amount:
      return [-1]

    for i in range(5):
      self.bank[i] -= withdraw[i]
    return withdraw


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(bankNoteCount)
# param_2 = obj.withdraw(amount)