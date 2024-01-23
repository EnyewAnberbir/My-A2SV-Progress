class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = 0
        maxcount = 0

        for i, block in enumerate(blocks):
            if block == 'B':
                count += 1
            if i >= k and blocks[i - k] == 'B':
                count -= 1
            maxcount = max(maxcount, count)

        return k - maxcount

        