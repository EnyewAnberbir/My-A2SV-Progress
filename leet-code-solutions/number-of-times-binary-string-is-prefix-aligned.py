class Solution:
  def numTimesAllBlue(self, flips: List[int]) -> int:
    ans = 0
    temp = 0

    for i, flip in enumerate(flips):
      temp = max(temp, flip)
      if temp == i + 1:
        ans += 1

    return ans