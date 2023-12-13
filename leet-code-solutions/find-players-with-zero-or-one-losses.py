class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = [[], []]
        count = {}

        for w, l in matches:
            count[w] = count.get(w, 0)
            count[l] = count.get(l, 0) + 1

        for i, no_lose in count.items():
            if no_lose < 2:
                ans[no_lose].append(i)

        return [sorted(ans[0]), sorted(ans[1])]
