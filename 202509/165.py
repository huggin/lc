class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        n = len(v1)
        m = len(v2)
        i, j = 0, 0
        while i < n or j < m:
            if i == n:
                if int(v2[j]) != 0:
                    return -1
                else:
                    j += 1
            elif j == m:
                if int(v1[i]) != 0:
                    return 1
                else:
                    i += 1
            elif int(v1[i]) < int(v2[j]):
                return -1
            elif int(v1[i]) > int(v2[j]):
                return 1
            else:
                i += 1
                j += 1
        return 0
