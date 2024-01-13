class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        temp = sum(cardPoints)
        summ = sum(cardPoints[:len(cardPoints)-k])
        res = temp - summ

        for right in range(k):
            summ -= cardPoints[right]
            summ += cardPoints[right+len(cardPoints)-k]
            res = max(res, temp - summ)

        return res