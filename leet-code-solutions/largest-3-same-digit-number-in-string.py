class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        for i in range(2, len(num)):
            string = ""
            if num[i] == num[i - 1] == num[i - 2]:
                string = num[i - 2:i + 1]

            if string and string > res:
                res = string

        return res
    

    
                
           

        