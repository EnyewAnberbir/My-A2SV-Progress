class Solution:
  def minimizeArrayValue(self, nums: List[int]) -> int:
    sol = 0
    prefix = 0

    for i, num in enumerate(nums):
      prefix += num
      average = math.ceil(prefix / (i + 1))
      sol = max(sol, average)

    return sol