class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.deleted = False

        sd = {}

        def insert(root, path):
            q = root
            for p in path:
                if p not in q.children:
                    q.children[p] = TrieNode()
                q = q.children[p]

        def dfs(q):
            if len(q.children) == 0:
                return ""
            cc = []
            for k, v in q.children.items():
                cc.append((k, dfs(v)))
            cc.sort()
            ans = []
            for name, ser in cc:
                ans.append(name)
                ans.append("$")
                ans.append(ser)
                ans.append("$")
            s = "".join(ans)
            if s not in sd:
                sd[s] = [q]
            else:
                sd[s].append(q)
            return s

        root = TrieNode()
        for path in paths:
            insert(root, path)

        dfs(root)
        for k, v in sd.items():
            if len(v) > 1:
                for q in v:
                    q.deleted = True

        ans = []
        curr = []

        def collectResults(q, curr):
            for k, v in q.children.items():
                if v.deleted:
                    continue
                curr.append(k)
                ans.append(curr[:])
                collectResults(v, curr)
                curr.pop()

        collectResults(root, curr)

        return ans
