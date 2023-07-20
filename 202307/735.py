class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for a in asteroids:
            flag = True
            if a < 0:
                while len(ans) > 0 and ans[-1] > 0:
                    if a < -ans[-1]:
                        ans.pop()
                    elif a == -ans[-1]:
                        ans.pop()
                        flag = False
                        break
                    else:
                        flag = False
                        break
            if flag:
                ans.append(a)

        return ans
