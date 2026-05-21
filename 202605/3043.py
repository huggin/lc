class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        class TrieNode:
            def __init__(self):
                self.children = [None] * 10

        trie = TrieNode()
        for a in set(arr1):
            s = str(a)
            p = trie
            for i in range(len(s)):
                j = ord(s[i]) - ord("0")
                if p.children[j] is None:
                    p.children[j] = TrieNode()
                p = p.children[j]

        ans = 0
        for a in set(arr2):
            s = str(a)
            p = trie
            flag = True
            for i in range(len(s)):
                j = ord(s[i]) - ord("0")
                if p.children[j] is None:
                    ans = max(ans, i)
                    flag = False
                    break
                p = p.children[j]
            if flag:
                ans = max(ans, len(s))

        return ans
