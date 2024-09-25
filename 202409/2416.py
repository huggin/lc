class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        class TrieNode:
            def __init__(self):
                self.children = [None] * 26
                self.count = 1

        root = TrieNode()
        for w in words:
            n = len(w)
            p = root
            for i in range(n):
                j = ord(w[i]) - ord("a")
                if p.children[j] is None:
                    p.children[j] = TrieNode()
                else:
                    p.children[j].count += 1
                p = p.children[j]

        ans = [0] * len(words)
        for k, w in enumerate(words):
            n = len(w)
            p = root
            for i in range(n):
                j = ord(w[i]) - ord("a")
                ans[k] += p.children[j].count
                p = p.children[j]

        return ans
