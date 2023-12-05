class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
            def difference(a, b):
                return abs(a[0] - b[0]) + abs(a[1] - b[1])

            dis = difference([0, 0], target)

            for ghost in ghosts:
                gdis = difference(ghost, target)
                if gdis <= dis:
                    return False

            return True
            