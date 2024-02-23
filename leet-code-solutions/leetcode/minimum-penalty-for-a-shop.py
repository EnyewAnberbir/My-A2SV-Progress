class Solution:
  def bestClosingTime(self, customers: str) -> int:
    res,val,maxval = 0,0,0
    for i, customer in enumerate(customers):
        if customer == 'Y' :
          val += 1 
        else:
            val -= 1
        if val > maxval:
            maxval = val
            res = i + 1

    return res