class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i = 0
        j = len(skill)-1
        temp = skill[0] + skill[len(skill)-1]
        summ = 0
        while i < j:
            if temp == skill[i]+skill[j]:
                summ += skill[i] * skill[j]
                i+=1
                j-=1
            else:
                return -1
                break
            
        return summ
            
        
            