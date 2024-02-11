class Solution:
  def minSubarray(self, nums: List[int], p: int) -> int:
    summ = sum(nums)
    rem = summ % p
    if rem == 0:
      return 0

    ans = len(nums)
    prefix = 0
    myDict = {0: -1}

    for i, num in enumerate(nums):
      prefix += num
      prefix %= p
      target = (prefix - rem + p) % p
      if target in myDict:
        ans = min(ans, i - myDict[target])
      myDict[prefix] = i
    if ans == len(nums):
        return -1
    else:
        return ans