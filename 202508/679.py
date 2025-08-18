class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        curr = []
        self.ans = False
        self.e = 1e-6

        def f1():
            t1 = [cards[0] + cards[1], cards[0] - cards[1], cards[0] * cards[1], cards[0]/cards[1]]
            t2 = [cards[2] + cards[3], cards[2] - cards[3], cards[2] * cards[3], cards[2]/cards[3]]

            for i in range(len(t1)):
                for j in range(len(t2)):
                    if abs(t1[i] * t2[j] - 24) <= self.e or abs(t1[i] + t2[j] - 24) < self.e or abs(t1[i] - t2[i] - 24) < self.e:
                        return True
                    if abs(t2[j]) > self.e and abs(t1[i] / t2[j] - 24) < self.e:
                        return True
            return False

        def f2():
            t1 = [cards[0] + cards[1], cards[0] - cards[1], cards[0] * cards[1], cards[0] / cards[1]]
            t2 = []
            for i in range(len(t1)):
                t2.append(t1[i] + cards[2])
                t2.append(t1[i] - cards[2])
                t2.append(t1[i] * cards[2])
                t2.append(t1[i] / cards[2])
            
            for i in range(len(t2)):
                if abs(t2[i] + cards[3] - 24) < self.e or abs(t2[i] -  cards[3] - 24) < self.e or abs(t2[i] * cards[3] - 24) < self.e or abs(t2[i] / cards[3] - 24) < self.e:
                    return True
            return False
        
        def f3():
            t1 = [cards[2] + cards[3], cards[2] - cards[3], cards[2] * cards[3], cards[2] / cards[3]]
            t2 = []
            for i in range(len(t1)):
                t2.append(cards[1] + t1[i])
                t2.append(cards[1] - t1[i])
                t2.append(cards[1] * t1[i])
                if abs(t1[i]) > self.e:
                    t2.append(cards[1] / t1[i])
            for i in range(len(t2)):
                if abs(cards[0] + t2[i] - 24) < self.e or abs(cards[0] - t2[i] - 24) < self.e or abs(cards[0] * t2[i] - 24) < self.e:
                    return True
                if t2[i] > self.e and abs(cards[0] / t2[i] - 24) < self.e:
                    return True
            return False

        def calc():
            if f1() or f2() or f3():
                self.ans = True

        def dfs(k):
            if self.ans:
                return
            if k == 4:
                calc()
                return

            for i in range(k, 4):
                cards[i], cards[k] = cards[k], cards[i]
                dfs(k+1)
                cards[i], cards[k] = cards[k], cards[i]

        dfs(0)
        return self.ans
        
