class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        j = 0
        ans = 0
        for p in players:
            while j < len(trainers) and p > trainers[j]:
                j += 1
            if j == len(trainers):
                break
            ans += 1
            j += 1
        return ans
