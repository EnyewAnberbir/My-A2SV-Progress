class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * len(boxes)

        follow, count = 0, 0
        for i in range(len(boxes)):
            ans[i] += follow
            count += 1 if boxes[i] == '1' else 0
            follow += count

        follow, count = 0, 0
        for i in range(len(boxes) - 1, -1, -1):
            ans[i] += follow
            count += 1 if boxes[i] == '1' else 0
            follow += count

        return ans
        