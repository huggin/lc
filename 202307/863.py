# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def solve2(self, p, k):
        if p is None:
            return

        if k == 0:
            self.ans.append(p.val)
            return
        else:
            self.solve2(p.left, k - 1)
            self.solve2(p.right, k - 1)

    def depth(self, root, target, k):
        if root is None:
            return 0

        if root.val == target.val:
            self.solve2(root, k)
            return 1

        left = self.depth(root.left, target, k)
        right = self.depth(root.right, target, k)
        if left == 0 and right == 0:
            return 0
        if left > 0:
            if k == left:
                self.ans.append(root.val)
            elif k > left:
                self.solve2(root.right, k - left - 1)
            return left + 1

        if right > 0:
            if k == right:
                self.ans.append(root.val)
            elif k > right:
                self.solve2(root.left, k - right - 1)
            return right + 1

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.ans = []
        self.depth(root, target, k)

        return self.ans
