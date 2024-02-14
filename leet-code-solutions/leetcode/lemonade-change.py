class Solution:
  def lemonadeChange(self, bills: List[int]) -> bool:
    count = 0
    count1= 0

    for bill in bills:
      if bill == 5:
        count += 1
      elif bill == 10:
        count -= 1
        count1+= 1
      else:  # bill == 20
        if count1> 0:
          count1-= 1
          count -= 1
        else:
          count -= 3
      if count < 0:
        return False

    return True