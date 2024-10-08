class Solution:
    def minSwaps(self, s: str) -> int:
        a = [c for c in s]
        i, j = 0, len(s) - 1
        curr = 0
        curr2 = 0
        ans = 0
        while i < j:
            if a[i] == "[":
                curr += 1
                i += 1
            elif curr > 0:
                curr -= 1
                i += 1
            else:
                while i < j:
                    if a[j] == "]":
                        curr2 += 1
                        j -= 1
                    elif curr2 > 0:
                        curr2 -= 1
                        j -= 1
                    else:
                        a[i], a[j] = a[j], a[i]
                        curr += 1
                        curr2 += 1
                        ans += 1
                        i += 1
                        j -= 1
                        break

        return ans


