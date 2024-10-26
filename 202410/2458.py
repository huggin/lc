# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        height = [0] * 100001

        def f(p):
            if p is None:
                return -1
            l = f(p.left)
            r = f(p.right)
            height[p.val] = max(l, r) + 1
            return height[p.val]

        res = [0] * 100001

        f(root)
        q = deque()
        q.append(root)
        level = 1
        while len(q) > 0:
            n = len(q)
            h = []
            nodes = []
            for _ in range(n):
                p = q.popleft()
                if p.left is not None:
                    h.append(height[p.left.val])
                    q.append(p.left)
                if p.right is not None:
                    h.append(height[p.right.val])
                    q.append(p.right)

            h.sort(reverse=True)
            if len(h) == 1:
                res[q[0].val] = level - 1
            else:
                for p in q:
                    if height[p.val] != h[0]:
                        res[p.val] = height[root.val]
                    else:
                        res[p.val] = level + h[1]
            level += 1

        ans = [0] * len(queries)
        for i in range(len(queries)):
            ans[i] = res[queries[i]]

        return ans
