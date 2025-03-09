class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        a = colors[:]
        n = len(a)
        for i in range(k-1):
            a.append(colors[i])
        
        j = 0
        i = 0
        ans = 0
        while i <= len(a) - k:
            flag = True
            for j in range(0, k-1):
                if a[j+i] == a[j+i+1]:
                    i = i + j + 1
                    flag = False
                    break
            if flag:
                i = i + k - 1
                ans += 1
                while flag:
                    i += 1
                    if i >= len(a) or a[i] == a[i-1]:
                        flag = False
                    if flag:
                        ans += 1

        return ans
