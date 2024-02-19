class Solution:
  def nextGreaterElements(self, nums: List[int]) -> List[int]:
    n = len(nums)
    res = [-1] * n
    stack = []  

    for i in range(n * 2):
      num = nums[i % n]
      while stack and nums[stack[-1]] < num:
        last = stack.pop()
        res[last] = num
      if i < n:
        stack.append(i)

    return res