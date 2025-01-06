class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        boxes = [0 if c == "0" else 1 for c in boxes]
        ans = [0] * n
        left = [0] * n
        left[0] = boxes[0]

        right = [0] * n
        right[n - 1] = boxes[n - 1]
        for i in range(1, n):
            left[i] += boxes[i] + left[i - 1]

        for i in range(n - 2, -1, -1):
            right[i] += boxes[i] + right[i + 1]

        ans[0] = sum(i * boxes[i] for i in range(n))
        for i in range(1, n):
            ans[i] = ans[i - 1] + left[i - 1] - right[i]

        return ans
