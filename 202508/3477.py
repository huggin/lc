class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        ans = 0
        n = len(fruits)
        used = [0] * n
        for i in range(n):
            flag = False
            for j in range(n):
                if used[j] == 0 and fruits[i] <= baskets[j]:
                    used[j] += 1
                    flag = True
                    break
            if not flag:
                ans += 1
        return ans
