class TreeNode:
    def __init__(self):
        self.children = [None] * 26
        self.val = -1


class Solution:
    def stringIndices(
        self, wordsContainer: List[str], wordsQuery: List[str]
    ) -> List[int]:
        root = TreeNode()
        for k, w in enumerate(wordsContainer):
            m = len(w)
            p = root
            for i in range(m - 1, -1, -1):
                if p.val == -1 or len(wordsContainer[p.val]) > m:
                    p.val = k
                j = ord(w[i]) - ord("a")
                if p.children[j] is None:
                    p.children[j] = TreeNode()
                p = p.children[j]
            if p.val == -1 or len(wordsContainer[p.val]) > m:
                p.val = k

        n = len(wordsQuery)
        ans = [0] * n
        for k, w in enumerate(wordsQuery):
            p = root
            m = len(w)
            for i in range(m - 1, -1, -1):
                j = ord(w[i]) - ord("a")
                if p.children[j] is None:
                    break
                else:
                    p = p.children[j]

            ans[k] = p.val

        return ans
