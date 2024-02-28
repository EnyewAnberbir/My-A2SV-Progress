class Solution:
  def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    myDict = {}
    stack = []  

    for num in nums2:
      while stack and stack[-1] < num:
        myDict[stack.pop()] = num
      stack.append(num)

    result_list = []
    for num in nums1:
        result_list.append(myDict.get(num, -1))
    return result_list