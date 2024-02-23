class Solution:
  def distance(self, nums: List[int]) -> List[int]:
    arr = [0] * len(nums)
    myDict = collections.defaultdict(list)

    for i, num in enumerate(nums):
      myDict[num].append(i)

    for j in myDict.values():
      n = len(j)
      if n == 1:
        continue
      summ = sum(j)
      left = 0
      for i in range(n):
        summ += (i - 1) * (j[i] - left)
        summ -= (n - 1 - i) * (j[i] - left)
        arr[j[i]] = summ
        left = j[i]

    return arr