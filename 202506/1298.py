class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        q = deque()
        lockedBox = set()
        currentKeys = set()
        for box in initialBoxes:
            if status[box] == 1:
                q.append(box)
            else:
                lockedBox.add(box)
        
        ans = 0
        while q:
            curr = q.pop()
            ans += candies[curr]
            for box in containedBoxes[curr]:
                if status[box] == 1:
                    q.append(box)
                elif box in currentKeys:
                    q.append(box)
                    currentKeys.remove(box)
                else:
                    lockedBox.add(box)

            for key in keys[curr]:
                if key in lockedBox:
                    q.append(key)
                    lockedBox.remove(key)
                else:
                    currentKeys.add(key)
        return ans

