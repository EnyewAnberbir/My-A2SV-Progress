class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        my_set = set(nums)
        max_len = 0
        
        for num in my_set:
            if num - 1 not in my_set:  
                temp_num = num
                length = 1

                while temp_num + 1 in my_set:  
                    temp_num += 1
                    length += 1

                max_len = max(max_len, length)

        return max_len
        
        

            


            
        



            



        



        