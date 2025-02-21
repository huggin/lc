# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.root.val = 0
        self.go(root)

    def go(self, p):
        if p.left:
            p.left.val = p.val * 2 + 1
            self.go(p.left)
        if p.right:
            p.right.val = p.val * 2 + 2
            self.go(p.right)

    def find(self, target: int) -> bool:
        return self.findv(self.root, target)

    def findv(self, p, target):
        if p is None:
            return False
        if p.val == target:
            return True

        return self.findv(p.left, target) or self.findv(p.right, target)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
