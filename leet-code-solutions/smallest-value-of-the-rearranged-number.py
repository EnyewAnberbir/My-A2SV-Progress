class Solution:
    def smallestNumber(self, num: int) -> int:
        if num >= 0:
            coll =[]
            for i in str(num):
                coll.append(i)
            coll.sort() 
            if len(coll) > 1 and int(coll[0]) ==0:
                for i in range(1, len(coll)):
                    if int(coll[i]) != 0:
                        coll[0], coll[i] = coll[i], coll[0] 
                        break
            coll1 = "".join(coll)       
            temp = int(coll1)
            return temp
        else:
            coll =[]
            string = str(num)
            for i in range(1, len(string)):
                coll.append(string[i])
            coll.sort()
            coll.reverse()

            coll1 = "".join(coll)
            temp = int(coll1)

            return 0 - temp
            
            
        