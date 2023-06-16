class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.count = 1


class Solution:
    def postOrder(self, p):
        if p is None:
            return 0
        left = self.postOrder(p.left)
        right = self.postOrder(p.right)
        if left == 0 and right == 0:
            return 1
        if left == 0:
            return right
        if right == 0:
            return left

        ans = (left * right * self.c[p.count - 1][p.left.count]) % self.m
        return ans

    def insert(self, root, val):
        if root is None:
            root = Node(val)
            return root

        p = root
        prev = None
        while p:
            prev = p
            p.count += 1
            if p.val > val:
                p = p.left
            else:
                p = p.right

        if prev.val > val:
            prev.left = Node(val)
        else:
            prev.right = Node(val)

        return root

    def numOfWays(self, nums: List[int]) -> int:
        self.m = int(1e9 + 7)
        n = len(nums)
        self.c = [[1 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, i):
                self.c[i][j] = (self.c[i - 1][j - 1] + self.c[i - 1][j]) % self.m

        root = None
        for v in nums:
            root = self.insert(root, v)

        return self.postOrder(root) - 1
