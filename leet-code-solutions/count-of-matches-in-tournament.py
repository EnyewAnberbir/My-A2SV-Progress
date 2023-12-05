class Solution:
    def numberOfMatches(self, n: int) -> int:
        tot = 0
        team = n
        while team >1 :
            if team%2 == 0:
                match = team //2 
                tot += match
                team -= team//2
            else:
                match = (team-1)//2
                tot += match
                team -= (team-1) //2
        return tot


            
        