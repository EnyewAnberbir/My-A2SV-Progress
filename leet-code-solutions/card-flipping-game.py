class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        n = len(fronts)
        card = set(fronts + backs)
        
        for i in range(n):
            if fronts[i] == backs[i]:
                card.discard(fronts[i])
        
        if not card:
            return 0
        
        return min(card)