class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts = Counter(answers)
        coll = 0

        for key, val in counts.items():
            same = val // (key + 1)
            coll += ((key + 1) * same)
            if val % (key + 1) != 0:
                coll += (key + 1)
        
        return coll
            


