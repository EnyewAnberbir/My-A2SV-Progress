class Solution:
  def numberOfWays(self, s: str) -> int:
    count = 0
    prefx_sum1 = [0] * 2
    prefix_sum2 = [0] * 2
    prefix_sum2[0] = s.count('0')
    prefix_sum2[1] = len(s) - prefix_sum2[0]

    for c in s:
      num = ord(c) - ord('0')
      prefix_sum2[num] -= 1
      if num == 0:
        count += prefx_sum1[1] * prefix_sum2[1]
      else:
        count += prefx_sum1[0] * prefix_sum2[0]
      prefx_sum1[num] += 1

    return count