class Solution:
  def countCompleteSubarrays(self, nums: List[int]) -> int:
    
    length = len(set(nums))
    count = collections.Counter()
    counter = 0

    l = 0
    for num in nums:
      count[num] += 1
      while len(count) == length:
        count[nums[l]] -= 1
        if count[nums[l]] == 0:
          del count[nums[l]]
        l += 1
      counter += l

    return counter