class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        sol = []
        temp = 0
        coll = [0] * (len(s) + 1)

        for start, end, direction in shifts:
            if direction:
                x =1
            else:
                x=-1
            coll[start] += x
            coll[end + 1] -= x
        
        for a, b in enumerate(s):
            temp = (temp + coll[a])%26
            num = (ord(s[a])-ord("a")+temp + 26) %26
            sol.append(chr(ord("a") + num))
        
        return "".join(sol)

        
        
       




















