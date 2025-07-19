class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans = []
        for f in folder:
            if (
                len(ans) == 0
                or len(ans[-1]) > len(f)
                or len(ans[-1]) == len(f)
                and ans[-1] != f
                or not f.startswith(ans[-1])
                or f[len(ans[-1])] != "/"
            ):
                ans.append(f)
        return ans
